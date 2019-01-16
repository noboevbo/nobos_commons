from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.skeleton_openpose import SkeletonOpenPose
from nobos_commons.data_structures.skeletons.skeleton_stickman import SkeletonStickman
from nobos_commons.tools.skeleton_converters.skeleton_converter_base import SkeletonConverter
from nobos_commons.utils.joint_helper import get_middle_joint


class SkeletonConverterOpenPoseToStickman(SkeletonConverter):
    def get_converted_skeleton(self, skeleton_openpose: SkeletonOpenPose) -> SkeletonStickman:
        skeleton_stickman: SkeletonStickman = self._get_skeleton_from_joints(skeleton_openpose)
        self._set_calculated_joints(skeleton_stickman)
        return skeleton_stickman

    # Private methods

    def _get_skeleton_from_joints(self, skeleton_openpose: SkeletonOpenPose) -> SkeletonStickman:
        skeleton_stickman: SkeletonStickman = SkeletonStickman()
        for joint in skeleton_openpose.joints:
            if hasattr(skeleton_stickman.joints, joint.name):
                skeleton_stickman.joints[joint.name].copy_from(joint, allow_different_num=True)
        return skeleton_stickman

    def _set_calculated_joints(self, skeleton_stickman: SkeletonStickman):
        calculated_hip_center: Joint2D = get_middle_joint(joint_a=skeleton_stickman.joints.left_hip,
                                                          joint_b=skeleton_stickman.joints.right_hip)

        if calculated_hip_center is not None:
            skeleton_stickman.joints.hip_center.copy_from(calculated_hip_center)
