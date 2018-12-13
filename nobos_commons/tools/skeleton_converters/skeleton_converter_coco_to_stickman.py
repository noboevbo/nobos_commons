from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.skeleton_coco import SkeletonCoco
from nobos_commons.data_structures.skeletons.skeleton_stickman import SkeletonStickman
from nobos_commons.tools.skeleton_converters.skeleton_converter_base import SkeletonConverter
from nobos_commons.utils.joint_helper import get_middle_joint


class SkeletonConverterCocoToStickman(SkeletonConverter):
    def get_converted_skeleton(self, skeleton_coco: SkeletonCoco) -> SkeletonStickman:
        skeleton_stickman: SkeletonStickman = self._get_skeleton_from_joints(skeleton_coco)
        self._set_calculated_joints(skeleton_stickman)
        return skeleton_stickman

    # Private methods

    def _get_skeleton_from_joints(self, skeleton_coco: SkeletonCoco) -> SkeletonStickman:
        skeleton_stickman: SkeletonStickman = SkeletonStickman()
        for joint in skeleton_coco.joints:
            skeleton_stickman.joints[joint.name].copy_from(joint, allow_different_num=True)
        return skeleton_stickman

    def _set_calculated_joints(self, skeleton_stickman: SkeletonStickman):
        calculated_neck: Joint2D = get_middle_joint(joint_a=skeleton_stickman.joints.left_shoulder,
                                                    joint_b=skeleton_stickman.joints.right_shoulder)

        calculated_hip_center: Joint2D = get_middle_joint(joint_a=skeleton_stickman.joints.left_hip,
                                                          joint_b=skeleton_stickman.joints.right_hip)
        if calculated_neck is not None:
            skeleton_stickman.joints.neck.copy_from(calculated_neck)

        if calculated_hip_center is not None:
            skeleton_stickman.joints.hip_center.copy_from(calculated_hip_center)
    #
    #
    # _coco_stickman_mapping = {
    #     'Nose': 'nose',
    #     'LEye': 'left_eye',
    #     'REye': 'right_eye',
    #     'LEar': 'left_ear',
    #     'REar': 'right_ear',
    #     'LShoulder': 'left_shoulder',
    #     'RShoulder': 'right_shoulder',
    #     'LElbow': 'left_elbow',
    #     'RElbow': 'right_elbow',
    #     'LWrist': 'left_wrist',
    #     'RWrist': 'right_wrist',
    #     'LHip': 'left_hip',
    #     'RHip': 'right_hip',
    #     'LKnee': 'left_knee',
    #     'RKnee': 'right_knee',
    #     'LAnkle': 'left_ankle',
    #     'RAnkle': 'right_ankle'
    # }
