import pickle
from typing import List

import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

from nobos_commons.data_structures.dimension import Vec3D
from nobos_commons.data_structures.human import Human
from nobos_commons.utils.visualization_helper import limb_should_be_displayed


# Adapted from: https://github.com/una-dinosauria/3d-pose-baseline/blob/master/src/viz.py

forward_vec = Vec3D(0, 0, 1)  # TODO: In commons?
current_animation = None

def __init_coordinate_system(ax: Axes3D, root_xyz: List[int], radius=2):
    ax.set_xlim3d([-radius + root_xyz[0], radius + root_xyz[0]])
    # ax.set_ylim3d([-radius + root_xyz[1], radius + root_xyz[1]])
    ax.set_ylim3d([0, 4]) # TODO no fixed values
    ax.set_zlim3d([-radius + root_xyz[2], radius + root_xyz[2]])

    # ax.set_xlabel("x")
    # ax.set_ylabel("z")
    # ax.set_zlabel("y")

    # Get rid of the ticks and tick labels
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    ax.get_xaxis().set_ticklabels([])
    ax.get_yaxis().set_ticklabels([])
    ax.set_zticklabels([])
    # ax.set_aspect('equal')

    # Get rid of the panes (actually, make them white)
    white = (0.0, 1.0, 0.0, 0.0)
    ax.w_xaxis.set_pane_color(white)
    ax.w_yaxis.set_pane_color(white)

    # Get rid of the lines in 3d
    ax.w_xaxis.line.set_color(white)
    ax.w_yaxis.line.set_color(white)
    ax.w_zaxis.line.set_color(white)


def plot_human(human: Human, plot_labels: bool = False):
    """
    Visualizes all human skeletons and straying joints / limbs in the image and displays the image.
    :param human: The human for which the skeleton should be drawn
    :param plot_labels: If true plots the joint names
    """
    fig = plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(111, projection='3d')

    _plot_human(ax, human, plot_labels)
    plt.show()

def _plot_human(ax: Axes3D, human: Human, plot_labels: bool = False):
    ax.clear()
    # TODO: GET ACTUAL ROOT by calculation, not just from joint 0..
    __init_coordinate_system(ax, [human.skeleton.joints[0].x, human.skeleton.joints[0].z, human.skeleton.joints[0].y])
    for limb in human.skeleton.limbs:
        if not limb_should_be_displayed(limb, human.skeleton.limb_colors, 0.4):
            continue
        x = [limb.joint_from.x, limb.joint_to.x]
        z = [limb.joint_from.z, limb.joint_to.z]
        y = [limb.joint_from.y, limb.joint_to.y]
        ax.plot(x, z, y, lw=2, c=human.skeleton.limb_colors[limb.num].hex)
    for joint in human.skeleton.joints:
        ax.scatter([joint.x], [joint.z], [joint.y], c=human.skeleton.joint_colors[joint.num].hex)
        if plot_labels:
            ax.text(joint.x, joint.z, joint.y, joint.name)

    #     if (joint.name == 'nose') and joint.rotation is not None:  # Display nose rotation vector as head direction indicator
    #         u, w, v = joint.rotation * forward_vec  # Switch x and z because y / z up diff
    #         ax.quiver(joint.x, joint.z, joint.y, u, v, w, length=0.5)
    # if human.root is not None:
    #     joint = human.root
    #     ax.scatter([joint.x], [joint.z], [joint.y], c=human.skeleton.joint_colors[joint.num].hex)
    #     if plot_labels:
    #         ax.text(joint.x, joint.z, joint.y, joint.name)
    #     u, w, v = joint.rotation * forward_vec  # Switch x and z because y / z up diff
    #     ax.quiver(joint.x, joint.z, joint.y, u, v, w, length=0.5)
    if human.skeleton.root is not None:
        ax.quiver(human.skeleton.root.x, human.skeleton.root.y, human.skeleton.root.z,
                  human.skeleton.root.direction_vec.x, human.skeleton.root.direction_vec.y, human.skeleton.root.direction_vec.z,
                  length=0.5)
    if human.skeleton.face is not None:
        ax.quiver(human.skeleton.face.x, human.skeleton.face.y, human.skeleton.face.z,
                  human.skeleton.face.direction_vec.x, human.skeleton.face.direction_vec.y, human.skeleton.face.direction_vec.z,
                  length=0.5)


def __animation_func(human: Human, ax: Axes3D, plot_labels: bool = False):
    _plot_human(ax, human, plot_labels)


def plot_animated_human(human_list: List[Human], plot_labels: bool = False):
    """
    Visualizes all human skeletons and straying joints / limbs in the image and displays the image.
    :param human: The human for which the skeleton should be drawn
    :param plot_labels: If true plots the joint names
    """
    global current_animation
    fig = plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(111, projection='3d')
    humantmp = human_list[0]
    __init_coordinate_system(ax, [humantmp.skeleton.joints[0].x, humantmp.skeleton.joints[0].z, humantmp.skeleton.joints[0].y])
    current_animation = animation.FuncAnimation(fig, __animation_func, human_list, fargs=(ax, plot_labels), interval=24)
    plt.show()