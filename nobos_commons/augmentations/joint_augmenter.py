import sys
from random import randint
from typing import List

import numpy as np

from nobos_commons.data_structures.dimension import ImageSize
from nobos_commons.data_structures.skeletons.joint_2d import Joint2D


class JointAugmenter(object):
    __slots__ = ['rotation_degrees', 'flip', 'image_size', 'random_position', 'transformation_matrix']

    def __init__(self, rotation_degrees: int, flip: bool, random_position: bool, image_size: ImageSize):
        self.rotation_degrees = rotation_degrees
        self.flip = flip
        self.image_size = image_size
        self.random_position = random_position
        self.transformation_matrix = self.__get_transformation_matrix()

    def get_augmented_joints(self, joints: List[Joint2D]):
        augmented_joints_coords: List[List[int]] = []

        for joint in joints:
            augmented_joints_coords.append([joint.x, joint.y])
        augmented_joints_coords = self.get_augmented_joint_list(augmented_joints_coords)

        augmented_joints: List[Joint2D] = []
        for joint_id, joint in enumerate(joints):
            augmented_joint_coords = augmented_joints_coords[joint_id]
            augmented_joints.append(Joint2D(x=augmented_joint_coords[0],
                                            y=augmented_joint_coords[1],
                                            num=joint.num,
                                            score=joint.score))

        # TODO: Random translate each joint
        return augmented_joints

    def get_augmented_joint_list(self, joint_list: List[List[int]]):
        augmented_joints_coords: List[List[int]] = []
        min_x = sys.maxsize
        min_y = sys.maxsize
        max_x = -sys.maxsize
        max_y = -sys.maxsize
        for joint in joint_list:
            augmented_joint_coords = np.matmul(self.transformation_matrix, np.array([joint[0], joint[1], 1]))
            x = augmented_joint_coords[0]
            y = augmented_joint_coords[1]
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
            augmented_joints_coords.append([augmented_joint_coords[0], augmented_joint_coords[1]])

        joint_box_width = int(abs(max_x - min_x))
        joint_box_height = int(abs(max_y - min_y))
        if self.random_position:
            new_upper_x = randint(0, self.image_size.width - joint_box_width)
            new_upper_y = randint(0, self.image_size.height - joint_box_height)
            translation_x = new_upper_x - min_x
            translation_y = new_upper_y - min_y
            translation_matrix = np.array([[1., 0., translation_x],
                                           [0., 1., translation_y],
                                           [0., 0., 1.]])
            translated_joints = []
            for augmented_joint_coords in augmented_joints_coords:
                translated_joint_coords = np.matmul(translation_matrix, np.array([augmented_joint_coords[0],
                                                                                 augmented_joint_coords[1],
                                                                                 1]))
                translated_joints.append([translated_joint_coords[0], translated_joint_coords[1]])
            augmented_joints_coords = translated_joints
        # TODO: Random translate each joint
        return augmented_joints_coords

    def __get_transformation_matrix(self) -> np.ndarray:
        A = np.cos(self.rotation_degrees / 180. * np.pi)
        B = np.sin(self.rotation_degrees / 180. * np.pi)

        # # Translate all joints to be centered arround coordinate system zero
        # center2zero = np.array([[1., 0., -center[0]],
        #                         [0., 1., -center[1]],
        #                         [0., 0., 1.]])

        rotate = np.array([[A, B, 0],
                           [-B, A, 0],
                           [0, 0, 1.]])

        flip = np.array([[-1 if self.flip else 1., 0., 0.],
                         [0., 1., 0.],
                         [0., 0., 1.]])

        # zero2center = np.array([[1., 0., center[0]],
        #                         [0., 1., center[1]],
        #                         [0., 0., 1.]])

        # order of combination is reversed
        combined = flip.dot(rotate)

        # TODO Random translation per joint
        return combined
