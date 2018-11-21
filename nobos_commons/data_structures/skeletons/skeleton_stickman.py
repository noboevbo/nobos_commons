from nobos_commons.data_structures.color import Color
from nobos_commons.data_structures.skeletons.skeleton_base import SkeletonBase
from nobos_commons.data_structures.skeletons.skeleton_stickman_joints import SkeletonStickmanJoints
from nobos_commons.data_structures.skeletons.skeleton_stickman_limbs import SkeletonStickmanLimbs


class SkeletonStickman(SkeletonBase):
    __slots__ = ['joints', 'limbs', 'joint_colors', 'limb_colors']

    def __init__(self):
        self.joints: SkeletonStickmanJoints = SkeletonStickmanJoints()
        self.limbs: SkeletonStickmanLimbs = SkeletonStickmanLimbs()
        self.joint_colors = [
            Color(r=192, g=192, b=192),  # ("Nose", 0),
            Color(r=128, g=128, b=128),  # ("Neck", 1),
            Color(r=255, g=0, b=0),  # ("RShoulder", 2),
            Color(r=255, g=51, b=51),  # ("RElbow", 3),
            Color(r=255, g=102, b=102),  # ("RWrist", 4),
            Color(r=0, g=255, b=0),  # ("LShoulder", 5),
            Color(r=51, g=255, b=51),  # ("LElbow", 6),
            Color(r=102, g=255, b=102),  # ("LWrist", 7),
            Color(r=102, g=0, b=0),  # ("RHip", 8),
            Color(r=153, g=0, b=0),  # ("RKnee", 9),
            Color(r=204, g=0, b=0),  # ("RAnkle", 10),
            Color(r=0, g=102, b=0),  # ("LHip", 11),
            Color(r=0, g=153, b=0),  # ("LKnee", 12),
            Color(r=0, g=204, b=0),  # ("LAnkle", 13),
            Color(r=255, g=0, b=255),  # ("REye", 14),
            Color(r=255, g=255, b=0),  # ("LEye", 15),
            Color(r=255, g=102, b=255),  # ("REar", 16),
            Color(r=255, g=255, b=102),  # ("LEar", 17),
            Color(r=64, g=64, b=64)  # ("Hip", 18)
        ]

        color_lower_left = Color(r=124, g=244, b=154)
        color_upper_left = Color(r=200, g=255, b=0)
        color_center = Color(r=255, g=254, b=228)
        color_lower_right = Color(r=250, g=2, b=60)
        color_upper_right = Color(r=252, g=157, b=154)

        self.limb_colors = [
            color_upper_right,  # 'Neck-RShoulder'
            color_upper_left,  # 'Neck-LShoulder'
            color_upper_right,  # 'RShoulder-RElbow'
            color_upper_right,  # 'RElbow-RWrist'
            color_upper_left,  # 'LShoulder-LElbow'
            color_upper_left,  # 'LElbow-LWrist'
            color_center,  # 'Neck-Hip'
            color_lower_right,  # 'Hip-RHip'
            color_lower_right,  # 'RHip-RKnee'
            color_lower_right,  # 'RKnee-RAnkle'
            color_lower_left,  # 'Hip-LHip'
            color_lower_left,  # 'LHip-LKnee'
            color_lower_left,  # 'LKnee-LAnkle'
            color_center,  # 'Neck-Nose'
            color_upper_right,  # 'Nose-REye'
            color_upper_right,  # 'REye-REar'
            color_upper_left,  # 'Nose-LEye'
            color_upper_left,  # 'LEye-LEar'
            None,  # 'RShoulder-REar'
            None  # 'LShoulder-LEar'
        ]

a = len(SkeletonStickman.joints)
x = 1

# def test() -> SkeletonBase:
#     return SkeletonStickman()
#
# a: SkeletonStickman = test()
# v = a.joints.nose
# b = 1
# test = SkeletonStickmanJoints()
# test[0] = 1
# print(test.nose)
# test["nose"] = 2
# print(test.nose)
# print(test[0])
# print(test['nose'])