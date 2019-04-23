import math
from typing import List, Dict, Tuple, Type

import cv2
import numpy as np
from nobos_commons.data_structures.dimension import ImageSize
from nobos_commons.data_structures.human import Human
from nobos_commons.data_structures.skeletons.skeleton_base import SkeletonBase
from nobos_commons.utils.bounding_box_helper import get_human_bounding_box_from_joints
from nobos_commons.utils.joint_helper import get_euclidean_distance_joint_lists


def get_features_to_track_from_human_joints(humans: List[Human]) -> np.ndarray:
    """
    TODO: Only use good features (joints with high scores)
    TODO: Alternative tracking without redetection via pose_net, just use pure tracked joints .. for win performance issues
    :param humans:
    :return:
    """
    features_to_track: List[List[float]] = []
    for human in humans:
        for joint in human.skeleton.joints:
            features_to_track.append([joint.x, joint.y])
    features_array = np.ndarray((len(features_to_track), 1, 2), dtype=np.float32)
    for feature_id, feature in enumerate(features_to_track):
        features_array[feature_id][0][0] = feature[0]
        features_array[feature_id][0][1] = feature[1]
    return features_array


class PoseTracker(object):
    __slots__ = ['image_size', 'skeleton_type', 'min_joint_score_for_similarity', 'lk_params',
                 'joint_acceptable_distance_scale_factor_human_size',
                 'next_human_uid', 'previous_frame_gray', 'min_human_score']

    def __init__(self, image_size: ImageSize, skeleton_type: Type[SkeletonBase],
                 min_joint_score_for_similarity: float = 0.5, min_human_score: float = 0.4):
        self.image_size = image_size
        self.skeleton_type = skeleton_type
        self.min_joint_score_for_similarity = min_joint_score_for_similarity
        self.joint_acceptable_distance_scale_factor_human_size = 0.075
        self.min_human_score = min_human_score
        # TODO: configurable?
        self.lk_params = dict(winSize=(15, 15),
                              maxLevel=2,
                              criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
        self.next_human_uid = 0
        self.previous_frame_gray: np.ndarray = None

    def get_humans_by_tracking(self, frame: np.ndarray, detected_humans: List[Human], previous_humans: List[Human]) -> Tuple[List[Human], List[Human]]:
        tracked_humans, self.previous_frame_gray = self._get_humans_by_tracking(frame, previous_humans)
        #
        # # TODO: This can be done in parallel:
        merged_humans_detected, _ = self.merge_humans(detected_humans, detected_humans,
                                                      assign_new_ids=False)  # Merge humans from detections which are similar
        merged_humans, undetected_humans = self.merge_humans(merged_humans_detected, tracked_humans)

        return merged_humans, undetected_humans

    def get_pose_similarity(self, human: Human, human2: Human) -> float:
        human_size = math.sqrt(math.pow(human.bounding_box.width, 2) + math.pow(human.bounding_box.height, 2))
        human2_size = math.sqrt(math.pow(human2.bounding_box.width, 2) + math.pow(human2.bounding_box.height, 2))
        if human_size > human2_size:
            max_acceptable_distance = human_size * self.joint_acceptable_distance_scale_factor_human_size
        else:
            max_acceptable_distance = human2_size * self.joint_acceptable_distance_scale_factor_human_size
        joint_similarity_percentages = []
        joint_distances = get_euclidean_distance_joint_lists(human.skeleton.joints, human2.skeleton.joints,
                                                             min_joint_score=self.min_joint_score_for_similarity)
        for joint_distance in joint_distances:
            # TODO: max_acceptable_distance something more meaningfull
            score = 1 - (joint_distance / max_acceptable_distance)
            if score < 0:
                score = 0
            joint_similarity_percentages.append(score)
        if len(joint_similarity_percentages) == 0:
            return 0
        return sum(joint_similarity_percentages) / len(joint_similarity_percentages)

    # TODO: Tracking on low res img...
    def _get_humans_by_tracking(self, frame: np.ndarray, previous_humans: List[Human]) -> (
            List[Human], np.ndarray):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        humans: List[Human] = []
        if previous_humans is not None and len(previous_humans) > 0:
            features_to_track = get_features_to_track_from_human_joints(previous_humans)
            points, st, err = cv2.calcOpticalFlowPyrLK(self.previous_frame_gray, frame_gray, features_to_track, None,
                                                       **self.lk_params)
            # # Select good points
            # good_new = p1[st == 1]
            # good_old = p0[st == 1]
            optical_flow_point_idx = 0
            for previous_human in previous_humans:
                skeleton = self.skeleton_type()
                for joint_num, point_idx in enumerate(range(optical_flow_point_idx, optical_flow_point_idx + len(
                        self.skeleton_type.joints))):
                    x = points[point_idx][0][0]
                    y = points[point_idx][0][1]
                    old_joint = previous_human.skeleton.joints[joint_num]
                    skeleton.joints[joint_num].x = int(x)
                    skeleton.joints[joint_num].y = int(y)
                    skeleton.joints[joint_num].score = old_joint.score
                humans.append(Human(uid=previous_human.uid,
                                    skeleton=skeleton,
                                    bounding_box=get_human_bounding_box_from_joints(skeleton.joints,
                                                                                    self.image_size.width,
                                                                                    self.image_size.height),
                                    ))

                optical_flow_point_idx = optical_flow_point_idx + len(self.skeleton_type.joints)
        return humans, frame_gray

    def merge_humans(self, humans_detected: List[Human], humans_tracked: List[Human],
                     assign_new_ids: bool = True) -> (List[Human], List[Human]):
        humans_by_similarity: Dict[Human, List[Tuple[float, Human]]] = {}
        pose_similarities: List[Tuple[float, Human]] = []
        for human_detected in humans_detected:
            for human_tracked in humans_tracked:
                if human_detected is not human_tracked:
                    pose_similarity = self.get_pose_similarity(human_detected, human_tracked)
                    pose_similarities.append((pose_similarity, human_detected))
                    if human_detected not in humans_by_similarity:
                        humans_by_similarity[human_detected] = [(pose_similarity, human_tracked)]
                    else:
                        humans_by_similarity[human_detected].append((pose_similarity, human_tracked))

        pose_similarities.sort(key=lambda x: x[0], reverse=True)
        # TODO REplace all this lists with obj
        final_humans_list: List[Human] = []
        final_human_uids: List[str] = []
        merged_humans: List[Human] = []
        for pose_tuple in pose_similarities:
            if pose_tuple[0] < 0.15:
                break
            human = pose_tuple[1]
            if human in merged_humans:
                continue
            for (similarity_score, similar_human) in humans_by_similarity[human]:
                # similarity_score = similar_human_tuple[0]
                if similarity_score < 0.15 or similar_human.uid in final_human_uids:
                    continue
                # similar_human = similar_human_tuple[1]
                if human not in final_humans_list:
                    if human.uid is None:
                        human.uid = similar_human.uid
                    else:
                        print("SOMETHING WRONG???? TRY TO MERGE A HUMAN WITH A OWN UID")
                    final_humans_list.append(human)
                    final_human_uids.append(human.uid)
                    merged_humans.append(similar_human)
                # merged_humans.append(similar_human)

        # Add detected but untracked humans and give them a new id
        for human in humans_detected:
            if human not in merged_humans and human not in final_humans_list:
                if assign_new_ids and human.uid is None:
                    human.uid = "{}".format(self.next_human_uid).zfill(5)
                    self.next_human_uid += 1
                final_humans_list.append(human)
                final_human_uids.append(human.uid)
        # Tracked but not detected humans:
        undetected_humans = []
        for human in humans_tracked:
            if human not in merged_humans and human.uid not in final_human_uids:
                undetected_humans.append(human)
        return final_humans_list, undetected_humans
        # Merge similar humans
