import math
from typing import List

import numpy

from nobos_commons.data_structures.geometry import Triangle
from nobos_commons.data_structures.skeletons.joint_3d import Joint3D
from nobos_commons.data_structures.skeletons.joint_visibility import JointVisibility


def get_euclidean_distance_joint3D(joint_a: Joint3D, joint_b: Joint3D) -> float:
    return numpy.linalg.norm(joint_a.to_numpy_position() - joint_b.to_numpy_position())


def get_euclidean_distance_joint_lists_3D(joints_a: List[Joint3D], joints_b: List[Joint3D],
                                          min_joint_score: float = 0.0) -> List[float]:
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
            joint_distances.append(get_euclidean_distance_joint3D(joint_a, joint_b))
    return joint_distances


def get_distances_3D(joint_a: Joint3D, joint_b: Joint3D) -> (float, float, float, float):
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
    distance_z = abs(joint_a.z - joint_b.z)
    euclidean_distance = get_euclidean_distance_joint3D(joint_a, joint_b)
    return distance_x, distance_y, distance_z, euclidean_distance


def get_triangle_from_joints_3D(joint_a: Joint3D, joint_b: Joint3D, joint_c: Joint3D) -> Triangle:
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
    length_a = get_euclidean_distance_joint3D(joint_c, joint_b)
    length_b = get_euclidean_distance_joint3D(joint_c, joint_a)
    length_c = get_euclidean_distance_joint3D(joint_a, joint_b)
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


def get_middle_joint_3D(joint_a: Joint3D, joint_b: Joint3D) -> Joint3D:
    """
    Returns a joint which is in the middle of the two input joints. The visibility and score is estimated by the
    visibility and score of the two surrounding joints.
    :param joint_a: Surrounding joint one
    :param joint_b: Surrounding joint two
    :return: Joint in the middle of joint_a and joint_b
    """
    if not joint_a.is_set or not joint_b.is_set:
        return None
    visibility: JointVisibility
    if joint_a.visibility == JointVisibility.VISIBLE and joint_b.visibility == JointVisibility.VISIBLE:
        visibility = JointVisibility.VISIBLE
    elif joint_a.visibility == JointVisibility.INVISIBLE or joint_b.visibility == JointVisibility.INVISIBLE:
        visibility = JointVisibility.INVISIBLE
    elif joint_a.visibility == JointVisibility.ABSENT or joint_b.visibility == JointVisibility.ABSENT:
        visibility = JointVisibility.ABSENT

    return Joint3D(
        x=int((joint_a.x + joint_b.x) / 2),
        y=int((joint_a.y + joint_b.y) / 2),
        z=int((joint_a.z + joint_b.z) / 2),
        score=(joint_a.score + joint_b.score) / 2,
        visibility=visibility
    )
