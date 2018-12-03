from typing import List

from nobos_commons.data_structures.human import Joint2D
from nobos_commons.data_structures.skeletons.joint_visibility import JointVisibility
from nobos_commons.data_structures.skeletons.skeleton_stickman_joints import SkeletonStickmanJoints
from nobos_commons.utils.joint_helper import get_middle_joint


class JointConverterJhmdbToStickman():
    def get_convertered_joints(self, jhmdb_joints: List[List[float]]) -> SkeletonStickmanJoints:
        skeleton_stickman_joints: SkeletonStickmanJoints = self._get_skeleton_from_joints(jhmdb_joints)
        self._set_calculated_joints(skeleton_stickman_joints)

    # Private methods

    def _get_skeleton_from_joints(self, jhmdb_joints: List[List[float]]) -> SkeletonStickmanJoints:
        skeleton_stickman_joints: SkeletonStickmanJoints = SkeletonStickmanJoints()
        for jhmdb_joint_id, jhmdb_joint_name in self._jhmdb_joint_names_ordered:
            internal_joint_name = self._jhmdb_stickman_mapping[jhmdb_joint_name]
            jhmdb_joint = jhmdb_joints[jhmdb_joint_id]
            skeleton_stickman_joints[internal_joint_name].x = jhmdb_joint[0]
            skeleton_stickman_joints[internal_joint_name].y = jhmdb_joint[1]
            skeleton_stickman_joints[internal_joint_name].visibility = JointVisibility.VISIBLE
            skeleton_stickman_joints[internal_joint_name].score = 1  # TODO: Add possibility to add other score
        return skeleton_stickman_joints

    def _set_calculated_joints(self, skeleton_stickman_joints: SkeletonStickmanJoints):
        a = 1
        # Hip Center
        calculated_hip_center: Joint2D = get_middle_joint(joint_a=skeleton_stickman_joints.left_hip,
                                                          joint_b=skeleton_stickman_joints.right_hip)
        if calculated_hip_center is not None:
            skeleton_stickman_joints.hip_center.copy_from(calculated_hip_center)

        # Nose

        # Left Eye

        # Left Ear

        # Right Eye

        # Right Ear

        # calculated_neck: Joint2D = get_middle_joint(joint_a=skeleton_stickman_joints.left_shoulder,
        #                                             joint_b=skeleton_stickman_joints.right_shoulder)
        #
        # calculated_hip_center: Joint2D = get_middle_joint(joint_a=skeleton_stickman_joints.left_hip,
        #                                                   joint_b=skeleton_stickman_joints.right_hip)
        # if calculated_neck is not None:
        #     skeleton_stickman_joints.neck.copy_from(calculated_neck)
        #
        # if calculated_hip_center is not None:
        #     skeleton_stickman_joints.hip_center.copy_from(calculated_hip_center)

    # Members

    _jhmdb_joint_names_ordered: List[str] = [
        'Neck',
        'Belly',
        'Head',
        'R_Shoulder',
        'L_Shoulder',
        'R_Hip',
        'L_Hip',
        'R_Elbow',
        'L_Elbow',
        'R_Knee',
        'L_Knee',
        'R_Wrist',
        'L_Wrist',
        'R_Ankle',
        'L_Ankle'
    ]

    _jhmdb_stickman_mapping = {
        'Head': 'nose',
        'Neck': 'neck',
        'L_Shoulder': 'left_shoulder',
        'R_Shoulder': 'right_shoulder',
        'L_Elbow': 'left_elbow',
        'R_Elbow': 'right_elbow',
        'L_Wrist': 'left_wrist',
        'R_Wrist': 'right_wrist',
        'L_Hip': 'left_hip',
        'R_Hip': 'right_hip',
        'L_Knee': 'left_knee',
        'R_Knee': 'right_knee',
        'L_Ankle': 'left_ankle',
        'R_Ankle': 'right_ankle'
    }
