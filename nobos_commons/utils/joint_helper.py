import math
from collections import OrderedDict
from typing import List, Dict, Type

from nobos_commons.data_structures.geometry import Triangle
from nobos_commons.data_structures.human import HumanPoseResult
from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.limb_2d import Limb2D
from nobos_commons.data_structures.skeletons.skeleton_base import SkeletonBase


def get_euclidean_distance_joint2d(joint_a: Joint2D, joint_b: Joint2D) -> float:
    return math.hypot(joint_b.x - joint_a.x, joint_b.y - joint_a.y)


def get_euclidean_distance_joint_lists(joints_a: List[Joint2D], joints_b: List[Joint2D], min_joint_score: float = 0.0) -> List[float]:
    """
    Returns the distance of the correspondiong joints of two lists. The lists must have the same length
    :param min_joint_score: The minimum score for both joints to be included in the distance check
    :param joints_a:
    :param joints_b:
    :return: List of floats for each joint_id in the lists with the euclidean distance
    """
    assert len(joints_a) == len(joints_b)
    joint_distances = []
    for joint_id, joint_tuple in enumerate(zip(joints_a, joints_b)):
        joint_a, joint_b = joint_tuple
        if joint_a.score >= min_joint_score and joint_b.score >= min_joint_score:
            joint_distances.append(get_euclidean_distance_joint2d(joint_a, joint_b))
    return joint_distances


def get_distances(joint_a: Joint2D, joint_b: Joint2D) -> (float, float, float):
    """
    Calculates the distances between the x and y coordinates as well as the euclidean distance between the joints.
    :param joint_a: 2D joint from
    :param joint_b: 2D joint to
    :return: (
    distance between the joint's x coordinates,
    distance between the joint's x coordinates,
    euclidean distance between the joints
    )
    """
    distance_x = abs(joint_a.x - joint_b.x)
    distance_y = abs(joint_a.y - joint_b.y)
    euclidean_distance = get_euclidean_distance_joint2d(joint_a, joint_b)
    return distance_x, distance_y, euclidean_distance


def get_angle_rad_between_joints(joint_a: Joint2D, joint_b: Joint2D) -> float:
    """
    Returns the angle between two joints in radians. Result between -pi and +pi
    """
    return math.atan2(joint_a.y - joint_b.y, joint_a.x - joint_b.x)


def get_triangle_from_joints(joint_a: Joint2D, joint_b: Joint2D, joint_c: Joint2D) -> Triangle:
    """
    Returns alpha, beta and gamma in a triangle formed by three joints (in radians).
    length_a = length_line c->b
    length_b = length_line c->a
    length_c = length_line a->b
    alpha = angle between joint_b and joint_c
    beta = angle between joint_a and joint_c
    gamma = angle between joint_a and joint_b
    cos alpha = (b^2 + c^2 - a^2) / (2 * b * c)
    cos beta = (a^2 + c^2 - b^2) / (2 * a * c)
    gamma = pi - alpha - beta
    :param joint_a: 2D joint
    :param joint_b: 2D joint
    :param joint_c: 2D joint
    :return: (alpha_rad, beta_rad, gamma_rad)
    """
    length_a = get_euclidean_distance_joint2d(joint_c, joint_b)
    length_b = get_euclidean_distance_joint2d(joint_c, joint_a)
    length_c = get_euclidean_distance_joint2d(joint_a, joint_b)
    # Note: Round to prevent round errors on later decimals on extremes (1.0, -1.0)
    # TODO: How to handle 0 distance correctly?
    if length_a == 0 or length_b == 0 or length_c == 0:
        return Triangle(0, 0, 0, 0, 0, 0)
    cos_alpha = round((((length_b ** 2) + (length_c ** 2) - (length_a ** 2)) / (2 * length_b * length_c)), 2)
    alpha_rad = math.acos(cos_alpha)
    cos_beta = round((((length_a ** 2) + (length_c ** 2) - (length_b ** 2)) / (2 * length_a * length_c)), 2)
    beta_rad = math.acos(cos_beta)
    gamma_rad = math.pi - alpha_rad - beta_rad
    return Triangle(length_a, length_b, length_c, alpha_rad, beta_rad, gamma_rad)


def get_limbs_from_joints(joints: Dict[int, Joint2D], skeleton_type: Type[SkeletonBase]) -> Dict[int, Limb2D]:
    limbs: Dict[int, Limb2D] = OrderedDict()
    # TODO: scores?
    for limb in skeleton_type.limbs:
        joint_from = joints[limb.joint_from.num]
        joint_to = joints[limb.joint_to.num]
        score_by_joints = (joint_from.score + joint_to.score) / 2
        limbs[limb.num] = Limb2D(num=limb.num,
                                 joint_from=joint_from,
                                 joint_to=joint_to,
                                 score=score_by_joints)
    return limbs


def get_human_from_joints(joints: Dict[int, Joint2D], skeleton_type: Type[SkeletonBase]):
    limbs = get_limbs_from_joints(joints, skeleton_type)
    # TODO: Human score .. calculate correctly
    human_score = 0
    for joint_id, joint in joints.items():
        human_score += joint.score
    human_score = human_score / len(skeleton_type.joints)
    skeleton = skeleton_type()
    skeleton.joints.copy_from_list(list(joints.values()))
    skeleton.limbs.set_limbs_from_list(list(limbs.values()))
    return HumanPoseResult(skeleton=skeleton, score=human_score)
