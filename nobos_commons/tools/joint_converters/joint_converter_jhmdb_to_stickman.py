from typing import List

from nobos_commons.data_structures.human import Joint2D
from nobos_commons.data_structures.skeletons.joint_visibility import JointVisibility
from nobos_commons.data_structures.skeletons.skeleton_stickman import SkeletonStickman
from nobos_commons.data_structures.skeletons.skeleton_stickman_joints import SkeletonStickmanJoints
from nobos_commons.utils.human_helper import get_human_from_joints
from nobos_commons.utils.human_surveyor import HumanSurveyor
from nobos_commons.utils.joint_helper import get_middle_joint


class JointConverterJhmdbToStickman():
    def __init__(self, human_surveyor: HumanSurveyor):
        self.human_surveyor = human_surveyor

    def get_convertered_joints(self, jhmdb_joints: List[List[float]]) -> SkeletonStickmanJoints:
        skeleton_stickman_joints: SkeletonStickmanJoints = self._get_skeleton_from_joints(jhmdb_joints)

        human = get_human_from_joints(skeleton_stickman_joints, SkeletonStickman)
        test = 1
        self._set_calculated_joints(skeleton_stickman_joints)

    # Private methods

    def _get_skeleton_from_joints(self, jhmdb_joints: List[List[float]]) -> SkeletonStickmanJoints:
        skeleton_stickman_joints: SkeletonStickmanJoints = SkeletonStickmanJoints()
        for jhmdb_joint_id, jhmdb_joint_name in enumerate(self._jhmdb_joint_names_ordered):
            if jhmdb_joint_name == 'Belly':  # Unused in stickman
                continue
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

        human_height = self.human_surveyor.get_human_height(skeleton_stickman)

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


joint = [[101.71333523, 81.88543806],
         [76.00189939, 114.05769629],
         [114.49979353, 75.64740069],
         [96.17142616, 94.39996673],
         [105.65714652, 95.77147671],
         [81.5999744, 127.7141945],
         [71.42858147, 128.62859578],
         [98.1139427, 120.38969526],
         [107.20052486, 116.06399233],
         [91.10690708, 161.60170212],
         [85.97002167, 164.1567473],
         [107.04635555, 139.74520041],
         [112.45755869, 137.48740878],
         [88.07904952, 197.41415193],
         [84.16994796, 197.65646189]]

a = JointConverterJhmdbToStickman(HumanSurveyor())

b = a.get_convertered_joints(joint)
v=1
