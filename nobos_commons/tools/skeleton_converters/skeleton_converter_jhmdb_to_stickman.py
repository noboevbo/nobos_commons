from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.skeleton_jhmdb import SkeletonJhmdb
from nobos_commons.data_structures.skeletons.skeleton_stickman import SkeletonStickman
from nobos_commons.tools.skeleton_converters.skeleton_converter_base import SkeletonConverter
from nobos_commons.utils.joint_helper import get_middle_joint


class SkeletonConverterJhmdbToStickman(SkeletonConverter):
    def get_converted_skeleton(self, skeleton_jhmdb: SkeletonJhmdb) -> SkeletonStickman:
        skeleton_stickman: SkeletonStickman = self._get_skeleton_from_joints(skeleton_jhmdb)
        self._set_calculated_joints(skeleton_stickman)
        return skeleton_stickman

    # Private methods

    def _get_skeleton_from_joints(self, skeleton_jhmdb: SkeletonJhmdb) -> SkeletonStickman:
        skeleton_stickman: SkeletonStickman = SkeletonStickman()
        for joint in skeleton_jhmdb.joints:
            if joint.name not in skeleton_stickman.joints.names:
                continue
            skeleton_stickman.joints[joint.name].copy_from(joint, allow_different_num=True)
        #  Head -> Nose
        skeleton_stickman.joints.nose.copy_from(skeleton_jhmdb.joints.head,
                                                allow_different_num=True,
                                                allow_different_name=True)
        return skeleton_stickman

    def _set_calculated_joints(self, skeleton_stickman: SkeletonStickman):
        a = 1
        # Hip Center
        calculated_hip_center: Joint2D = get_middle_joint(joint_a=skeleton_stickman.joints.left_hip,
                                                          joint_b=skeleton_stickman.joints.right_hip)
        if calculated_hip_center is not None:
            skeleton_stickman.joints.hip_center.copy_from(calculated_hip_center)

        # Neck
        calculated_neck: Joint2D = get_middle_joint(joint_a=skeleton_stickman.joints.left_shoulder,
                                                    joint_b=skeleton_stickman.joints.right_shoulder)
        if calculated_neck is not None:
            skeleton_stickman.joints.neck.copy_from(calculated_neck)

        # TODO: Calculate eyes and ears by body metrics and camera viewpoint
        # Left Eye

        # Left Ear

        # Right Eye

        # Right Ear

    # Members

    # _jhmdb_joint_names_ordered: List[str] = [
    #     'Neck',
    #     'Belly',
    #     'Head',
    #     'R_Shoulder',
    #     'L_Shoulder',
    #     'R_Hip',
    #     'L_Hip',
    #     'R_Elbow',
    #     'L_Elbow',
    #     'R_Knee',
    #     'L_Knee',
    #     'R_Wrist',
    #     'L_Wrist',
    #     'R_Ankle',
    #     'L_Ankle'
    # ]
    #
    # _jhmdb_stickman_mapping = {
    #     'head': 'nose',
    #     'neck': 'neck',
    #     'left_shoulder': 'left_shoulder',
    #     'right_shoulder': 'right_shoulder',
    #     'left_elbow': 'left_elbow',
    #     'right_elbow': 'right_elbow',
    #     'left_wrist': 'left_wrist',
    #     'right_wrist': 'right_wrist',
    #     'left_hip': 'left_hip',
    #     'right_hip': 'right_hip',
    #     'left_knee': 'left_knee',
    #     'R_Knee': 'right_knee',
    #     'L_Ankle': 'left_ankle',
    #     'R_Ankle': 'right_ankle'
    # }

# joint = [[101.71333523, 81.88543806],
#          [76.00189939, 114.05769629],
#          [114.49979353, 75.64740069],
#          [96.17142616, 94.39996673],
#          [105.65714652, 95.77147671],
#          [81.5999744, 127.7141945],
#          [71.42858147, 128.62859578],
#          [98.1139427, 120.38969526],
#          [107.20052486, 116.06399233],
#          [91.10690708, 161.60170212],
#          [85.97002167, 164.1567473],
#          [107.04635555, 139.74520041],
#          [112.45755869, 137.48740878],
#          [88.07904952, 197.41415193],
#          [84.16994796, 197.65646189]]
#
# test =
