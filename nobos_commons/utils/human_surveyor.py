from nobos_commons.data_structures.skeletons.limb_2d import Limb2D
from nobos_commons.data_structures.skeletons.skeleton_stickman_limbs import SkeletonStickmanLimbs
from nobos_commons.utils.limb_helper import get_limb_length


class HumanSurveyor(object):
    def get_human_height(self, limbs: SkeletonStickmanLimbs) -> float:
        bone_name, bone = self._get_bone_for_measurement(limbs)
        bone_length = get_limb_length(bone)
        return self._bone_measurements_to_person_heights[bone_name](bone_length)

    def _get_bone_for_measurement(self, limbs: SkeletonStickmanLimbs) -> (str, Limb2D):
        """
        Returns femur, tibia, humerus or radius in this order. Depends on if the bones are recognized or not
        """
        if limbs.right_hip_to_right_knee is not None:
            return "femur", limbs.right_hip_to_right_knee
        if limbs.left_hip_to_left_knee is not None:
            return "femur", limbs.left_hip_to_left_knee

        if limbs.right_knee_to_right_ankle is not None:
            return "tibia", limbs.right_knee_to_right_ankle
        if limbs.left_knee_to_left_ankle is not None:
            return "tibia", limbs.left_knee_to_left_ankle

        if limbs.right_shoulder_to_right_elbow is not None:
            return "humerus", limbs.right_shoulder_to_right_elbow
        if limbs.left_shoulder_to_left_elbow is not None:
            return "humerus", limbs.left_shoulder_to_left_elbow

        if limbs.right_elbow_to_right_wrist is not None:
            return "femur", limbs.right_elbow_to_right_wrist
        if limbs.left_elbow_to_left_wrist is not None:
            return "femur", limbs.left_elbow_to_left_wrist

        return None, None

    _bone_measurements_to_person_heights = {
        "femur": lambda bone_length: 4 * bone_length,
        "tibia": lambda bone_length: 4.44 * bone_length,
        "humerus": lambda bone_length: 4.7 * bone_length,
        "radius": lambda bone_length: 6.66 * bone_length
    }
