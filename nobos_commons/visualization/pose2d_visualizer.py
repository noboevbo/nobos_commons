import math
from typing import List, Dict

import cv2
import numpy as np

from nobos_commons.data_structures.color import Color, Colors
from nobos_commons.data_structures.human import ImageContentHumans
from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.limb_2d import Limb2D


def visualize_human_pose(original_img: np.ndarray, human_data: ImageContentHumans, limb_colors: [], joint_colors: [],
                         wait_for_ms: int = 0, min_limb_score_to_show: float = 0.4):
    """
    Visualizes all human skeletons and straying joints / limbs in the image and displays the image.
    :param original_img: The original image
    :param human_data: The human content in the image
    :param limb_colors: The colors of the limbs to visualize
    :param joint_colors: The colors of the joints to visualize
    :param min_limb_score_to_show: The minimum score of limbs to be displayed
    :param wait_for_ms: The time for which the image should be displayed, if zero wait for keypress
    :return: The image with the visualized humans and straying joints / limbs
    """
    img = get_human_pose_image(original_img, human_data, limb_colors, joint_colors, min_limb_score_to_show)
    cv2.imshow("human_pose", img)
    cv2.waitKey(wait_for_ms)


def save_human_pose_img(original_img: np.ndarray, human_data: ImageContentHumans, limb_colors: [], joint_colors: [],
                        file_path="human_pose.png", min_limb_score_to_show: float = 0.4):
    """
    Visualizes all human skeletons and straying joints / limbs in the image and saves the image to the given path.
    :param original_img: The original image
    :param human_data: The human content in the image
    :param limb_colors: The colors of the limbs to visualize
    :param joint_colors: The colors of the joints to visualize
    :param file_path: The path in which the image with the visualized content should be saved.
    :param min_limb_score_to_show: The minimum score of limbs to be displayed
    :return: The image with the visualized humans and straying joints / limbs
    """
    img = get_human_pose_image(original_img, human_data, limb_colors, joint_colors, min_limb_score_to_show)
    cv2.imwrite(file_path, img)


def get_human_pose_image(original_img: np.ndarray, human_data: ImageContentHumans, limb_colors: List[Color],
                         joint_colors: List[Color], min_limb_score_to_show):
    """
    Visualizes all human skeletons and straying joints / limbs in the image and returns it.
    :param original_img: The original image
    :param human_data: The human content in the image
    :param limb_colors: The colors of the limbs to visualize
    :param joint_colors: The colors of the joints to visualize
    :param min_limb_score_to_show: The minimum score of limbs to be displayed
    :return: The image with the visualized humans and straying joints / limbs
    """
    img = original_img.copy()
    limb_line_width = 4

    for human in human_data.humans:
        for idx, limb in enumerate(human.skeleton.limbs):
            if not limb:
                continue
            if limb.matched_score < min_limb_score_to_show:
                continue
            limb_color = limb_colors[limb.num]
            if limb_color is None:
                continue
            img = visualize_limb(img, limb, limb_color, limb_line_width, True)
        for joint_num, joint in enumerate(human.skeleton.joints):
            cv2.circle(img, tuple(joint.coordinates), 5, joint_colors[joint_num].tuple_bgr, thickness=-1)
    return img


def visualize_limb(original_img: np.ndarray, limb: Limb2D, limb_color: Color, line_width: int = 4,
                   write_in_original_image: bool = False):
    """
    Visualizes the limb with the given color and line width.
    :param original_img: The original image
    :param limb: The limb to visualize
    :param limb_color: The color in which the limb should be displayed
    :param line_width: The width of the line visualizing the limb
    :param write_in_original_image: Whether to write in the original img or create a copy of the image
    :return: The image with the visualized joints
    """
    img = original_img if write_in_original_image else original_img.copy()
    cur_canvas = img.copy()
    X = [limb.joint_from.y, limb.joint_to.y]
    Y = [limb.joint_from.x, limb.joint_to.x]
    mX = np.mean(X)
    mY = np.mean(Y)
    length = ((X[0] - X[1]) ** 2 + (Y[0] - Y[1]) ** 2) ** 0.5
    angle = math.degrees(math.atan2(X[0] - X[1], Y[0] - Y[1]))
    polygon = cv2.ellipse2Poly((int(mY), int(mX)), (int(length / 2), line_width), int(angle), 0, 360, 1)
    cv2.fillConvexPoly(cur_canvas, polygon, limb_color.tuple_bgr)
    img = cv2.addWeighted(img, 0.1, cur_canvas, 0.9, 0)
    return img


def visualize_straying_joints(original_img: np.ndarray, straying_joint_dict: Dict[int, List[Joint2D]],
                              joint_colors: List[Color], write_in_original_image: bool = False):
    """
    Visualizes joints which are not assigned to a skeleton. They will be displayed with gray color, background.
    :param original_img: The original image
    :param straying_joint_dict: dictionary with key: joint_num and value: List[Joint2D]
    :param joint_colors: The color list for each joint_num
    :param write_in_original_image: Whether to write in the original img or create a copy of the image
    :return: The image with the visualized joints
    """
    img = original_img if write_in_original_image else original_img.copy()
    for joint_num, straying_joints in straying_joint_dict.items():
        img = visualize_joints(original_img=img,
                               joints=straying_joints,
                               color=Colors.grey,
                               write_in_original_image=True,
                               radius=10)
        img = visualize_joints(original_img=img,
                               joints=straying_joints,
                               color=joint_colors[joint_num],
                               write_in_original_image=True,
                               radius=5)
    return img


def visualize_joint(original_img: np.ndarray, joint: Joint2D, color: Color, write_in_original_image: bool = False,
                    radius: int = 5):
    """
    Visualizes the given joint with the given color and radius.
    :param original_img: The original image
    :param joint: The joint to visualize
    :param color: The color in which the joints should be displayed
    :param write_in_original_image: Whether to write in the original img or create a copy of the image
    :param radius: The radius of the joint circles
    :return: The image with the visualized joint
    """
    img = original_img if write_in_original_image else original_img.copy()
    img = cv2.circle(img, tuple(joint.coordinates), radius, color.tuple_bgr, thickness=-1)
    return img


def visualize_joints(original_img: np.ndarray, joints: List[Joint2D], color: Color,
                     write_in_original_image: bool = False,
                     radius: int = 5):
    """
    Visualizes joints with the given color and radius.
    :param original_img: The original image
    :param joints: List of joints
    :param color: The color in which the joints should be displayed
    :param write_in_original_image: Whether to write in the original img or create a copy of the image
    :param radius: The radius of the joint circles
    :return: The image with the visualized joints
    """
    img = original_img if write_in_original_image else original_img.copy()
    for joint in joints:
        img = visualize_joint(img, joint, color, write_in_original_image=False, radius=radius)
    return img
