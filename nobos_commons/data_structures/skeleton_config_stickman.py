from nobos_commons.data_structures.color import Color
from nobos_commons.data_structures.skeleton_config_base import SkeletonConfigBase
from collections import defaultdict, OrderedDict


def ltr_parts(parts_dict):
    # when we flip image left parts became right parts and vice versa. This is the list of parts to exchange each other.
    left_parts = [parts_dict[p] for p in
                  ["LShoulder", "LElbow", "LWrist", "LHip", "LKnee", "LAnkle", "LEye", "LEar"]]
    right_parts = [parts_dict[p] for p in
                   ["RShoulder", "RElbow", "RWrist", "RHip", "RKnee", "RAnkle", "REye", "REar"]]
    return left_parts, right_parts


class SkeletonConfigStickman(SkeletonConfigBase):
    joints = OrderedDict([
        ("Nose", 0),
        ("Neck", 1),
        ("RShoulder", 2),
        ("RElbow", 3),
        ("RWrist", 4),
        ("LShoulder", 5),
        ("LElbow", 6),
        ("LWrist", 7),
        ("RHip", 8),
        ("RKnee", 9),
        ("RAnkle", 10),
        ("LHip", 11),
        ("LKnee", 12),
        ("LAnkle", 13),
        ("REye", 14),
        ("LEye", 15),
        ("REar", 16),
        ("LEar", 17),
        ("Hip", 18)
    ])

    limbs = [
        [1, 2],  # 'Neck-RShoulder'
        [1, 5],  # 'Neck-LShoulder'
        [2, 3],  # 'RShoulder-RElbow'
        [3, 4],  # 'RElbow-RWrist'
        [5, 6],  # 'LShoulder-LElbow'
        [6, 7],  # 'LElbow-LWrist'
        [1, 18],  # 'Neck-Hip'
        [18, 8],  # 'Hip-RHip'
        [8, 9],  # 'RHip-RKnee'
        [9, 10],  # 'RKnee-RAnkle'
        [18, 11],  # 'Hip-LHip'
        [11, 12],  # 'LHip-LKnee'
        [12, 13],  # 'LKnee-LAnkle'
        [1, 0],  # 'Neck-Nose'
        [0, 14],  # 'Nose-REye'
        [14, 16],  # 'REye-REar'
        [0, 15],  # 'Nose-LEye'
        [15, 17],  # 'LEye-LEar'
        [2, 16],  # 'RShoulder-REar'
        [5, 17]  # 'LShoulder-LEar'
    ]

    joint_is_source_in_limb = defaultdict(list)
    joint_is_target_in_limb = defaultdict(list)
    joint_names = []
    for joint_name, joint_num in joints.items():
        joint_names.append(joint_name)
        for limb_nr, limb in enumerate(limbs):
            if limb[0] == joint_num:
                joint_is_source_in_limb[joint_num].append(limb_nr)
            if limb[1] == joint_num:
                joint_is_target_in_limb[joint_num].append(limb_nr)

    limb_names = []
    __joint_list = list(joints.items())
    for limb in limbs:
        limb_names.append("{}-{}".format(__joint_list[limb[0]][0], __joint_list[limb[1]][0]))
    limb_names.append("Background")

    color_lower_left = Color(r=124, g=244, b=154)
    color_upper_left = Color(r=200, g=255, b=0)
    color_center = Color(r=255, g=254, b=228)
    color_lower_right = Color(r=250, g=2, b=60)
    color_upper_right = Color(r=252, g=157, b=154)

    limb_colors = [
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

    left_parts, right_parts = ltr_parts(joints)
