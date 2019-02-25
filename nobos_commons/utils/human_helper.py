from collections import defaultdict
from typing import Dict, List, Type

from nobos_commons.data_structures.human import Human
from nobos_commons.data_structures.image_content import ImageContent
from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.limb_2d import Limb2D
from nobos_commons.data_structures.skeletons.skeleton_base import SkeletonBase
from nobos_commons.utils.limb_helper import get_limbs_from_joints


def is_joint_from_limb_in_human(human: Human, limb_candidate: Limb2D) -> bool:
    return human.skeleton.joints[limb_candidate.joint_from.num] == limb_candidate.joint_from or \
           human.skeleton.joints[limb_candidate.joint_to.num] == limb_candidate.joint_to


def get_empty_human(num_joints, num_limbs) -> Human:
    human = Human([None] * num_joints, [None] * num_limbs)
    return human


def are_joints_in_both_humans(human_a: Human, human_b: Human) -> bool:
    for joint_idx, joint in enumerate(human_b.skeleton.joints):
        if joint is not None and human_a.skeleton.joints[joint_idx] is not None:
            return True
    return False


def get_merged_humans(human_a: Human, human_b: Human) -> Human:
    for joint_idx, joint in enumerate(human_b.skeleton.joints):
        if joint is None:
            continue
        if human_a.skeleton.joints[joint_idx] is not None:
            raise RuntimeError("Merge conflict, joint exists in both humans")
        human_a.skeleton.joints[joint_idx].copy_from(joint)

    for limb_idx, limb in enumerate(human_b.skeleton.limbs):
        if limb is None:
            continue
        if human_a.skeleton.limbs[limb_idx] is not None:
            raise RuntimeError("Merge conflict, limb exists in both humans")  #
        human_a.skeleton.limbs[limb_idx].copy_from(limb)

    human_a.score += human_b.score
    return human_a


def get_humans_from_limbs(limbs: Dict[int, List[Limb2D]], skeleton_type: Type[SkeletonBase], min_number_of_limbs: int,
                          min_human_score: float) -> (List[Human], Dict[int, List[Limb2D]]):
    # last number in each row is the total parts number of that person
    # the second last number in each row is the score of the overall configuration
    human_list: List[Human] = []  # Humans n, 20
    limbs_used: List[Limb2D] = []

    for limb_nr, limb_candidates in limbs.items():
        for i, limb_candidate in enumerate(limb_candidates):
            found = 0
            subset_idx = [-1, 1]
            for j in range(len(human_list)):
                if is_joint_from_limb_in_human(human_list[j], limb_candidate):
                    subset_idx[found] = j
                    found += 1
            if found == 1:
                j = subset_idx[0]
                if human_list[j].skeleton.joints[limb_candidate.joint_to.num] != limb_candidate.joint_to:
                    human_list[j].skeleton.joints[limb_candidate.joint_to.num].copy_from(limb_candidate.joint_to)
                    human_list[j].skeleton.limbs[limb_candidate.num].copy_from(limb_candidate)
                    if limb_candidate not in limbs_used:
                        limbs_used.append(limb_candidate)
                    human_list[j].score += limb_candidate.score + limb_candidate.joint_to.score

            elif found == 2:
                j1, j2 = subset_idx
                # print("found = 2")
                if not are_joints_in_both_humans(human_list[j1], human_list[j2]):
                    human_list[j1] = get_merged_humans(human_list[j1], human_list[j2])
                    del human_list[j2]
                else:  # as like found == 1
                    human_list[j1].skeleton.joints[limb_candidate.joint_to.num].copy_from(limb_candidate.joint_to)
                    human_list[j1].skeleton.limbs[limb_candidate.num].copy_from(limb_candidate)
                    if limb_candidate not in limbs_used:
                        limbs_used.append(limb_candidate)
                    human_list[j1].score += limb_candidate.score + limb_candidate.joint_to.score
            elif not found:
                human = get_empty_human(len(skeleton_type.joints), len(skeleton_type.limbs))
                human.skeleton.joints[limb_candidate.joint_from.num].copy_from(limb_candidate.joint_from)   # TODO: may be removed
                human.skeleton.joints[limb_candidate.joint_to.num].copy_from(limb_candidate.joint_to)  # TODO: may be removed
                human.skeleton.limbs[limb_candidate.num].copy_from(limb_candidate)
                if limb_candidate not in limbs_used:
                    limbs_used.append(limb_candidate)
                human.score = limb_candidate.matched_score
                human_list.append(human)

    # Remove humnans which have too low number of limbs or a too low total limb score.
    # cfg.pose_estimator.skeleton_limb_score
    # cfg.pose_estimator.skeleton_min_limbs
    deleteIdx = []
    for i in range(len(human_list)):
        if human_list[i].skeleton.limbs.num_limbs_set < min_number_of_limbs or \
                (human_list[i].score / human_list[i].skeleton.limbs.num_limbs_set) < min_human_score:
            deleteIdx.append(i)
    humans = [x for i, x in enumerate(human_list) if i not in deleteIdx]

    # Collect limbs which aren't contained in a human, TODO: DOESNT INCLUDE THE ONES FROM DELETE HUMANS!
    straying_limbs: Dict[int, List[Limb2D]] = defaultdict(list)
    for limb_num, limb_list in limbs.items():
        for limb in limb_list:
            if limb not in limbs_used:
                straying_limbs[limb_num].append(limb)

    return humans, straying_limbs


def get_human_from_joints(joints: Dict[int, Joint2D], skeleton_type: Type[SkeletonBase]) -> Human:
    """
    TODO: Remove this? Replaced by auto_set_limbs in skeleton.
    :param joints:
    :param skeleton_type:
    :return:
    """
    limbs = get_limbs_from_joints(joints, skeleton_type)
    # TODO: Human score .. calculate correctly
    human_score = 0
    for joint_id, joint in joints.items():
        human_score += joint.score
    human_score = human_score / len(skeleton_type.joints)
    skeleton = skeleton_type()
    # skeleton.joints.copy_from_list(list(joints.values()))  # Implicitly copied when limbs are copied
    skeleton.limbs.copy_from_other(limbs)
    return Human(skeleton=skeleton, score=human_score)


def get_human_with_highest_score(image_content: ImageContent):
    """
    Returns the human with the highest score from image_content
    :param image_content:
    :return:
    """
    if len(image_content.humans) > 0:
        if len(image_content.humans) > 1:
            print("Detected more than one human, use only one.")
        human_idx_to_use = 0
        best_score = 0
        for human_idx, human in enumerate(image_content.humans):
            if human.score > best_score:
                human_idx_to_use = human_idx
        return image_content.humans[human_idx_to_use]

    return None
