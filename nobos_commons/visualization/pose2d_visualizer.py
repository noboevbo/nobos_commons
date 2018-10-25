import math
from typing import List, Tuple

import numpy as np
import cv2

from nobos_commons.data_structures.bounding_box import BoundingBox
from nobos_commons.data_structures.constants.color_palette import DETECTION_COLOR_PALETTE
from nobos_commons.data_structures.constants.detection_classes import COCO_CLASSES
from nobos_commons.data_structures.human import ImageContentHumans, Joint2D


def visualize_human_pose(original_img: np.ndarray, human_data: ImageContentHumans, limb_colors: [],
                         wait_for_ms: int = 0):
    img = get_human_pose_image(original_img, human_data, limb_colors)
    cv2.imshow("human_pose", img)
    cv2.waitKey(wait_for_ms)


def save_human_pose_img(original_img: np.ndarray, human_data: ImageContentHumans, limb_colors: [],
                        file_path="human_pose.png"):
    img = get_human_pose_image(original_img, human_data, limb_colors)
    cv2.imwrite(file_path, img)


def get_human_pose_image(ori_img: np.ndarray, human_data: ImageContentHumans, limb_colors: []):
    image = ori_img.copy()
    add_img_title(image, "Humans: {}".format(len(human_data.humans)))
    # TODO: MARK STRAYING STUFF!
    for joint_num, straying_joints in human_data.straying_joints.items():
        for straying_joint in straying_joints:
            cv2.circle(image, tuple(straying_joint.coordinates), 4, limb_colors[joint_num], thickness=1)  # TODO: Uses LimbColors

    # TODO: DRAW STRAYING LIMBS!
    stickwidth = 4

    for human in human_data.humans:
        for idx, limb in enumerate(human.limbs):
            if not limb:
                continue
            if limb.matched_score < 0.4: # TODO COnfigurable thresh
                continue
            # if limb['limb'] not in [[1,5], [1,2]]:
            #     continue
            color = limb_colors[limb.num]
            if color is None:
                continue
            color = [color[2], color[1], color[0]]
            #color = [0, 85, 255]
            cur_canvas = image.copy()
            X = [limb.joint_from.y, limb.joint_to.y]
            Y = [limb.joint_from.x, limb.joint_to.x]
            cv2.circle(image, (limb.joint_from.x, limb.joint_from.y), 4, color, thickness=-1)
            cv2.circle(image, (limb.joint_to.x, limb.joint_to.y), 4, color, thickness=-1)
            mX = np.mean(X)
            mY = np.mean(Y)
            length = ((X[0] - X[1]) ** 2 + (Y[0] - Y[1]) ** 2) ** 0.5
            angle = math.degrees(math.atan2(X[0] - X[1], Y[0] - Y[1]))
            polygon = cv2.ellipse2Poly((int(mY), int(mX)), (int(length / 2), stickwidth), int(angle), 0, 360, 1)
            cv2.fillConvexPoly(cur_canvas, polygon, color)
            image = cv2.addWeighted(image, 0.1, cur_canvas, 0.9, 0)
    return image


def visualize_joints(original_img: np.ndarray, joints: List[Joint2D], color: Tuple[int, int, int]):
    joint_img = original_img.copy()
    for joint in joints:
        cv2.circle(joint_img, tuple(joint.coordinates), 4, color, thickness=1)
    return joint_img