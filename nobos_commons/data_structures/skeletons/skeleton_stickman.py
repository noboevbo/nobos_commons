from nobos_commons.data_structures.color import Color
from nobos_commons.data_structures.skeletons.skeleton_base import SkeletonBase
from nobos_commons.data_structures.skeletons.skeleton_stickman_joints import SkeletonStickmanJoints
from nobos_commons.data_structures.skeletons.skeleton_stickman_limbs import SkeletonStickmanLimbs


class SkeletonStickman(SkeletonBase):
    joints: SkeletonStickmanJoints = SkeletonStickmanJoints()
    limbs: SkeletonStickmanLimbs = SkeletonStickmanLimbs()
    joint_colors = [
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

    limb_colors = [
        Color(r=252, g=157, b=154),  # 'Neck-RShoulder'
        Color(r=200, g=255, b=0),  # 'Neck-LShoulder'
        Color(r=252, g=157, b=154),  # 'RShoulder-RElbow'
        Color(r=252, g=157, b=154),  # 'RElbow-RWrist'
        Color(r=200, g=255, b=0),  # 'LShoulder-LElbow'
        Color(r=200, g=255, b=0),  # 'LElbow-LWrist'
        Color(r=255, g=254, b=228),  # 'Neck-Hip'
        Color(r=250, g=2, b=60),  # 'Hip-RHip'
        Color(r=250, g=2, b=60),  # 'RHip-RKnee'
        Color(r=250, g=2, b=60),  # 'RKnee-RAnkle'
        Color(r=124, g=244, b=154),  # 'Hip-LHip'
        Color(r=124, g=244, b=154),  # 'LHip-LKnee'
        Color(r=124, g=244, b=154),  # 'LKnee-LAnkle'
        Color(r=255, g=254, b=228),  # 'Neck-Nose'
        Color(r=252, g=157, b=154),  # 'Nose-REye'
        Color(r=252, g=157, b=154),  # 'REye-REar'
        Color(r=200, g=255, b=0),  # 'Nose-LEye'
        Color(r=200, g=255, b=0),  # 'LEye-LEar'
        None,  # 'RShoulder-REar'
        None  # 'LShoulder-LEar'
    ]

test = SkeletonStickman.__dict__.keys()
test2 = SkeletonStickman.joints.__dict__.keys()
a = len(SkeletonStickman.joints)
x = 1

# class A(object):
#     a: int = 1
#
#     def __init__(self):
#         self.a = 2
#
# a = A()
# print(a.a)
# print(A.a)
#
# test = SkeletonStickman()
# test.vasd = 1
# a = test
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