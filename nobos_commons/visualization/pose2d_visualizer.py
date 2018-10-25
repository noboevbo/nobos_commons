import math
from typing import List, Tuple, Dict

import numpy as np
import cv2

from nobos_commons.data_structures.human import ImageContentHumans, Joint2D, Limb2D
from nobos_commons.visualization.img_utils import rgb_to_bgr_color


def visualize_human_pose(original_img: np.ndarray, human_data: ImageContentHumans, limb_colors: [],
                         wait_for_ms: int = 0):
    img = get_human_pose_image(original_img, human_data, limb_colors)
    cv2.imshow("human_pose", img)
    cv2.waitKey(wait_for_ms)


def save_human_pose_img(original_img: np.ndarray, human_data: ImageContentHumans, limb_colors: [], joint_colors: [],
                        file_path="human_pose.png"):
    img = get_human_pose_image(original_img, human_data, limb_colors, joint_colors)
    cv2.imwrite(file_path, img)


def get_human_pose_image(original_img: np.ndarray, human_data: ImageContentHumans, limb_colors: [], joint_colors: []):
    img = original_img.copy()
    stickwidth = 4

    for human in human_data.humans:
        for idx, limb in enumerate(human.limbs):
            if not limb:
                continue
            if limb.matched_score < 0.4: # TODO COnfigurable thresh
                continue
            limb_color = limb_colors[limb.num]
            if limb_color is None:
                continue
            limb_color = rgb_to_bgr_color(limb_color)
            img = visualize_limb(img, limb, limb_color, stickwidth, True)
        for joint_num, joint in enumerate(human.joints):
            cv2.circle(img, tuple(joint.coordinates), 5, joint_colors[joint_num], thickness=-1)
    return img


def visualize_limb(original_img: np.ndarray, limb: Limb2D, limb_color: List[int], stickwidth: int = 4, write_in_original_image: bool = False):
    img = original_img if write_in_original_image else original_img.copy()
    cur_canvas = img.copy()
    X = [limb.joint_from.y, limb.joint_to.y]
    Y = [limb.joint_from.x, limb.joint_to.x]
    mX = np.mean(X)
    mY = np.mean(Y)
    length = ((X[0] - X[1]) ** 2 + (Y[0] - Y[1]) ** 2) ** 0.5
    angle = math.degrees(math.atan2(X[0] - X[1], Y[0] - Y[1]))
    polygon = cv2.ellipse2Poly((int(mY), int(mX)), (int(length / 2), stickwidth), int(angle), 0, 360, 1)
    cv2.fillConvexPoly(cur_canvas, polygon, limb_color)
    img = cv2.addWeighted(img, 0.1, cur_canvas, 0.9, 0)
    return img


def visualize_straying_joints(original_img: np.ndarray, straying_joint_dict: Dict[int, List[Joint2D]], joint_colors: [], write_in_original_image: bool = False):
    img = original_img if write_in_original_image else original_img.copy()
    for joint_num, straying_joints in straying_joint_dict.items():
        # TODO: Mark straying joints somehow? Thicker? Thinner?
        visualize_joints(original_img=img,
                         joints=straying_joints,
                         color=joint_colors[joint_num],
                         write_in_original_image=True)


def visualize_joints(original_img: np.ndarray, joints: List[Joint2D], color: Tuple[int, int, int], write_in_original_image: bool = False):
    img = original_img if write_in_original_image else original_img.copy()
    for joint in joints:
        cv2.circle(img, tuple(joint.coordinates), 5, color, thickness=-1)
    return img