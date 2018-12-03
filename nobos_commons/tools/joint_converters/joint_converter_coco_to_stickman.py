from typing import List

from nobos_commons.data_structures.human import Joint2D
from nobos_commons.data_structures.skeletons.joint_visibility import JointVisibility
from nobos_commons.data_structures.skeletons.skeleton_stickman_joints import SkeletonStickmanJoints
from nobos_commons.utils.joint_helper import get_middle_joint


class JointConverterCocoToStickman():
    def get_convertered_joints(self, coco_joints: List[List[float]]) -> SkeletonStickmanJoints:
        skeleton_stickman_joints: SkeletonStickmanJoints = self._get_skeleton_from_joints(coco_joints)
        self._set_calculated_joints(skeleton_stickman_joints)

    # Private methods

    def _get_skeleton_from_joints(self, coco_joints: List[List[float]]) -> SkeletonStickmanJoints:
        skeleton_stickman_joints: SkeletonStickmanJoints = SkeletonStickmanJoints()
        for coco_joint_id, coco_joint_name in self._coco_joint_names_ordered:
            internal_joint_name = self._coco_stickman_mapping[coco_joint_name]
            coco_joint = coco_joints[coco_joint_id]
            skeleton_stickman_joints[internal_joint_name].x = coco_joint[0]
            skeleton_stickman_joints[internal_joint_name].y = coco_joint[1]
            skeleton_stickman_joints[internal_joint_name].visibility = JointVisibility(coco_joint[2])
            skeleton_stickman_joints[internal_joint_name].score = 1  # TODO: Add possibility to add other score
        return skeleton_stickman_joints

    def _set_calculated_joints(self, skeleton_stickman_joints: SkeletonStickmanJoints):
        calculated_neck: Joint2D = get_middle_joint(joint_a=skeleton_stickman_joints.left_shoulder,
                                                    joint_b=skeleton_stickman_joints.right_shoulder)

        calculated_hip_center: Joint2D = get_middle_joint(joint_a=skeleton_stickman_joints.left_hip,
                                                          joint_b=skeleton_stickman_joints.right_hip)
        if calculated_neck is not None:
            skeleton_stickman_joints.neck.copy_from(calculated_neck)

        if calculated_hip_center is not None:
            skeleton_stickman_joints.hip_center.copy_from(calculated_hip_center)

    # Members

    _coco_joint_names_ordered: List[str] = [
        'Nose',
        'LEye',
        'REye',
        'LEar',
        'REar',
        'LShoulder',
        'RShoulder',
        'LElbow',
        'RElbow',
        'LWrist',
        'RWrist',
        'LHip',
        'RHip',
        'LKnee',
        'RKnee',
        'LAnkle',
        'RAnkle'
    ]

    _coco_stickman_mapping = {
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
