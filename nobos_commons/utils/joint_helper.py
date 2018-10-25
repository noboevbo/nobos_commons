import math
from typing import List

from nobos_commons.data_structures.human import Joint2D


def get_euclidean_distance_joint2d(joint_a: Joint2D, joint_b: Joint2D) -> float:
    return math.hypot(joint_b.x - joint_a.x, joint_b.y - joint_a.y)


def get_joint_distances(joints_a: List[Joint2D], joints_b: List[Joint2D], min_joint_score: float = 0.0) -> List[float]:
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
