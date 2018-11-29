from nobos_commons.data_structures.skeletons.limb_2d import Limb2D
from nobos_commons.data_structures.skeletons.skeleton_limbs_base import SkeletonLimbsBase
from nobos_commons.data_structures.skeletons.skeleton_stickman_joints import SkeletonStickmanJoints


class SkeletonStickmanLimbs(SkeletonLimbsBase):
    __slots__ = [
        '_neck_to_right_shoulder'
        '_neck_to_left_shoulder'
        '_right_shoulder_to_right_elbow'
        '_right_elbow_to_right_wrist'
        '_left_shoulder_to_left_elbow'
        '_left_elbow_to_left_wrist'
        '_neck_to_hip_center'
        '_hip_center_to_right_hip'
        '_right_hip_to_right_knee'
        '_right_knee_to_right_ankle'
        '_hip_center_to_left_hip'
        '_left_hip_to_left_knee'
        '_left_knee_to_left_ankle'
        '_neck_to_nose'
        '_nose_to_right_eye'
        '_right_eye_to_right_ear'
        '_nose_to_left_eye'
        '_left_eye_to_left_ear'
        '_right_shoulder_to_right_ear'
        '_left_shoulder_to_left_ear'
    ]

    def __init__(self, skeleton_joints: SkeletonStickmanJoints):
        self._neck_to_right_shoulder: Limb2D = Limb2D(num=0,
                                                      joint_from=skeleton_joints.neck,
                                                      joint_to=skeleton_joints.right_shoulder)
        self._neck_to_left_shoulder: Limb2D = Limb2D(num=1,
                                                     joint_from=skeleton_joints.neck,
                                                     joint_to=skeleton_joints.left_shoulder)
        self._right_shoulder_to_right_elbow: Limb2D = Limb2D(num=2,
                                                             joint_from=skeleton_joints.right_shoulder,
                                                             joint_to=skeleton_joints.right_elbow)
        self._right_elbow_to_right_wrist: Limb2D = Limb2D(num=3,
                                                          joint_from=skeleton_joints.right_elbow,
                                                          joint_to=skeleton_joints.right_wrist)
        self._left_shoulder_to_left_elbow: Limb2D = Limb2D(num=4,
                                                           joint_from=skeleton_joints.left_shoulder,
                                                           joint_to=skeleton_joints.left_elbow)
        self._left_elbow_to_left_wrist: Limb2D = Limb2D(num=5,
                                                        joint_from=skeleton_joints.left_elbow,
                                                        joint_to=skeleton_joints.left_wrist)
        self._neck_to_hip_center: Limb2D = Limb2D(num=6,
                                                  joint_from=skeleton_joints.neck,
                                                  joint_to=skeleton_joints.hip_center)
        self._hip_center_to_right_hip: Limb2D = Limb2D(num=7,
                                                       joint_from=skeleton_joints.hip_center,
                                                       joint_to=skeleton_joints.right_hip)
        self._right_hip_to_right_knee: Limb2D = Limb2D(num=8,
                                                       joint_from=skeleton_joints.right_hip,
                                                       joint_to=skeleton_joints.right_knee)
        self._right_knee_to_right_ankle: Limb2D = Limb2D(num=9,
                                                         joint_from=skeleton_joints.right_knee,
                                                         joint_to=skeleton_joints.right_ankle)
        self._hip_center_to_left_hip: Limb2D = Limb2D(num=10,
                                                      joint_from=skeleton_joints.hip_center,
                                                      joint_to=skeleton_joints.left_hip)
        self._left_hip_to_left_knee: Limb2D = Limb2D(num=11,
                                                     joint_from=skeleton_joints.left_hip,
                                                     joint_to=skeleton_joints.left_knee)
        self._left_knee_to_left_ankle: Limb2D = Limb2D(num=12,
                                                       joint_from=skeleton_joints.left_knee,
                                                       joint_to=skeleton_joints.left_ankle)
        self._neck_to_nose: Limb2D = Limb2D(num=13,
                                            joint_from=skeleton_joints.neck,
                                            joint_to=skeleton_joints.nose)
        self._nose_to_right_eye: Limb2D = Limb2D(num=14,
                                                 joint_from=skeleton_joints.nose,
                                                 joint_to=skeleton_joints.right_eye)
        self._right_eye_to_right_ear: Limb2D = Limb2D(num=15,
                                                      joint_from=skeleton_joints.right_eye,
                                                      joint_to=skeleton_joints.right_ear)
        self._nose_to_left_eye: Limb2D = Limb2D(num=16,
                                                joint_from=skeleton_joints.nose,
                                                joint_to=skeleton_joints.left_eye)
        self._left_eye_to_left_ear: Limb2D = Limb2D(num=17,
                                                    joint_from=skeleton_joints.left_eye,
                                                    joint_to=skeleton_joints.left_ear)
        self._right_shoulder_to_right_ear: Limb2D = Limb2D(num=18,
                                                           joint_from=skeleton_joints.right_shoulder,
                                                           joint_to=skeleton_joints.right_ear)
        self._left_shoulder_to_left_ear: Limb2D = Limb2D(num=19,
                                                         joint_from=skeleton_joints.left_shoulder,
                                                         joint_to=skeleton_joints.left_ear)

    @property
    def neck_to_right_shoulder(self) -> Limb2D:
        return self._neck_to_right_shoulder

    @property
    def neck_to_left_shoulder(self) -> Limb2D:
        return self._neck_to_left_shoulder

    @property
    def right_shoulder_to_right_elbow(self) -> Limb2D:
        return self._right_shoulder_to_right_elbow

    @property
    def right_elbow_to_right_wrist(self) -> Limb2D:
        return self._right_elbow_to_right_wrist

    @property
    def left_shoulder_to_left_elbow(self) -> Limb2D:
        return self._left_shoulder_to_left_elbow

    @property
    def left_elbow_to_left_wrist(self) -> Limb2D:
        return self._left_elbow_to_left_wrist

    @property
    def neck_to_hip_center(self) -> Limb2D:
        return self._neck_to_hip_center

    @property
    def hip_center_to_right_hip(self) -> Limb2D:
        return self._hip_center_to_right_hip

    @property
    def right_hip_to_right_knee(self) -> Limb2D:
        return self._right_hip_to_right_knee

    @property
    def right_knee_to_right_ankle(self) -> Limb2D:
        return self._right_knee_to_right_ankle

    @property
    def hip_center_to_left_hip(self) -> Limb2D:
        return self._hip_center_to_left_hip

    @property
    def left_hip_to_left_knee(self) -> Limb2D:
        return self._left_hip_to_left_knee

    @property
    def left_knee_to_left_ankle(self) -> Limb2D:
        return self._left_knee_to_left_ankle

    @property
    def neck_to_nose(self) -> Limb2D:
        return self._neck_to_nose

    @property
    def nose_to_right_eye(self) -> Limb2D:
        return self._nose_to_right_eye

    @property
    def right_eye_to_right_ear(self) -> Limb2D:
        return self._right_eye_to_right_ear

    @property
    def nose_to_left_eye(self) -> Limb2D:
        return self._nose_to_left_eye

    @property
    def left_eye_to_left_ear(self) -> Limb2D:
        return self._left_eye_to_left_ear

    @property
    def right_shoulder_to_right_ear(self) -> Limb2D:
        return self._right_shoulder_to_right_ear

    @property
    def left_shoulder_to_left_ear(self) -> Limb2D:
        return self._left_shoulder_to_left_ear
