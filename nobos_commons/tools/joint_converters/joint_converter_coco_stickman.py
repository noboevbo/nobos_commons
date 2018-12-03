from collections import OrderedDict
from typing import List, Dict

import numpy as np

from nobos_commons.data_structures.human import Joint2D
from nobos_commons.data_structures.skeletons.skeleton_stickman import SkeletonStickman


def get_internal_middle_joint_visibility(joints, both_side_joints_known, r_joint, l_joint):
    return np.minimum(joints[both_side_joints_known, r_joint, 2], joints[both_side_joints_known, l_joint, 2])


def get_internal_middle_joint_position(joints, both_shoulders_known, r_shoulder, l_shoulder):
    return (joints[both_shoulders_known, r_shoulder, 0:2] + joints[both_shoulders_known, l_shoulder, 0:2]) / 2


class JointConverterCocoStickman(JointConverterBase):
    coco_joints = {
        'Nose': 0,
        'LEye': 1,
        'REye': 2,
        'LEar': 3,
        'REar': 4,
        'LShoulder': 5,
        'RShoulder': 6,
        'LElbow': 7,
        'RElbow': 8,
        'LWrist': 9,
        'RWrist': 10,
        'LHip': 11,
        'RHip': 12,
        'LKnee': 13,
        'RKnee': 14,
        'LAnkle': 15,
        'RAnkle': 16
    }

    coco_stickman_mapping = {
        'Nose': 'nose',
        'LEye': 'left_eye',
        'REye': 'right_eye',
        'LEar': 'left_ear',
        'REar': 'right_ear',
        'LShoulder': 'left_shoulder',
        'RShoulder': 'right_shoulder',
        'LElbow': 'left_elbow',
        'RElbow': 'right_elbow',
        'LWrist': 'left_wrist',
        'RWrist': 'right_wrist',
        'LHip': 'left_hip',
        'RHip': 'right_hip',
        'LKnee': 'left_knee',
        'RKnee': 'right_knee',
        'LAnkle': 'left_ankle',
        'RAnkle': 'right_ankle'
    }

    def get_converted_joint_list(self, source_joints: []) -> np.array:
        """
        This method is used by dataset, with coco GT nobos_commons.data_structures
        :param source_joints:
        :return:
        """
        joints = np.array(source_joints)
        result = np.zeros((joints.shape[0], len(SkeletonStickman.joints), 3), dtype=np.float)
        result[:, :, 2] = 2.  # 2 - absent, 1 visible, 0 - invisible

        for coco_joint, coco_joint_id in self.coco_joints.items():
            internal_joint_id = SkeletonStickman.joints[coco_joint]
            assert internal_joint_id != 1, "Neck shouldn't be known yet"
            result[:, internal_joint_id, :] = joints[:, coco_joint_id, :]

        neck_internal_joint_num = SkeletonStickman.joints.neck.num
        r_shoulder_coco = self.coco_joints['RShoulder']
        l_shoulder_coco = self.coco_joints['LShoulder']

        # no neck in coco database, we calculate it as average of shoulders
        # TODO: we use 0 - hidden, 1 visible, 2 absent - it is not coco values they processed by generate_hdf5
        both_shoulders_known = (joints[:, l_shoulder_coco, 2] < 2) & (joints[:, r_shoulder_coco, 2] < 2)
        result[both_shoulders_known, neck_internal_joint_num, 0:2] = get_internal_middle_joint_position(joints,
                                                                                                        both_shoulders_known,
                                                                                                        r_shoulder_coco,
                                                                                                        l_shoulder_coco)
        result[both_shoulders_known, neck_internal_joint_num, 2] = get_internal_middle_joint_position(joints,
                                                                                                      both_shoulders_known,
                                                                                                      r_shoulder_coco,
                                                                                                      l_shoulder_coco)

        hip_internal_joint_num = SkeletonStickman.joints.hip_center.num
        r_hip_coco = self.coco_joints['RHip']
        l_hip_coco = self.coco_joints['LHip']

        both_hips_known = (joints[:, l_hip_coco, 2] < 2) & (joints[:, r_hip_coco, 2] < 2)

        result[both_hips_known, hip_internal_joint_num, 0:2] = get_internal_middle_joint_position(joints,
                                                                                                  both_hips_known,
                                                                                                  r_hip_coco,
                                                                                                  l_hip_coco)
        result[both_hips_known, hip_internal_joint_num, 2] = get_internal_middle_joint_position(joints, both_hips_known,
                                                                                                r_hip_coco, l_hip_coco)

        return result

    def get_converted_joints(self, coco_joints: List[List[float]], joint_scores: List[float]) -> Dict[int, Joint2D]:
        results: Dict[int, Joint2D] = {}
        for coco_joint_name, coco_joint_id in self.coco_joints.items():
            internal_joint_name = self.coco_stickman_mapping[coco_joint_name]  # TODO I NEED THE CORRECT MAPPING HERE
            coco_joint = coco_joints[coco_joint_id]
            stickman_joint = SkeletonStickman.joints[internal_joint_name]
            results[stickman_joint.num] = Joint2D(num=stickman_joint.num,
                                                  name=stickman_joint.name,
                                                  x=int(coco_joint[0]),
                                                  y=int(coco_joint[1]),
                                                  score=joint_scores[coco_joint_id])

        r_shoulder_coco = coco_joints[self.coco_joints['RShoulder']]
        l_shoulder_coco = coco_joints[self.coco_joints['LShoulder']]
        r_shoulder_score = joint_scores[self.coco_joints['RShoulder']]
        l_shoulder_score = joint_scores[self.coco_joints['LShoulder']]
        results[SkeletonStickman.joints.neck.num] = Joint2D(num=SkeletonStickman.joints.neck.num,
                                                            name=SkeletonStickman.joints.neck.name,
                                                            x=int((r_shoulder_coco[0] + l_shoulder_coco[0]) / 2),
                                                            y=int((r_shoulder_coco[1] + l_shoulder_coco[1]) / 2),
                                                            score=(r_shoulder_score + l_shoulder_score) / 2)

        r_hip_coco = coco_joints[self.coco_joints['RHip']]
        l_hip_coco = coco_joints[self.coco_joints['LHip']]
        r_hip_score = joint_scores[self.coco_joints['RHip']]
        l_hip_score = joint_scores[self.coco_joints['LHip']]
        results[SkeletonStickman.joints.hip_center.num] = Joint2D(num=SkeletonStickman.joints.hip_center.num,
                                                                  name=SkeletonStickman.joints.hip_center.name,
                                                                  x=int((r_hip_coco[0] + l_hip_coco[0]) / 2),
                                                                  y=int((r_hip_coco[1] + l_hip_coco[1]) / 2),
                                                                  score=(r_hip_score + l_hip_score) / 2)

        return OrderedDict(sorted(results.items()))
