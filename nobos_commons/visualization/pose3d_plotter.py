import pickle
from typing import List

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from nobos_commons.data_structures.human import Human
from nobos_commons.data_structures.skeletons.skeleton_stickman_3d import SkeletonStickman3D
from nobos_commons.utils.visualization_helper import limb_should_be_displayed

# Adapted from: https://github.com/una-dinosauria/3d-pose-baseline/blob/master/src/viz.py


def __init_coordinate_system(ax: Axes3D, root_xyz: List[int], radius=2):
    # TODO: GET ACTUAL ROOT, HOW TO?
    ax.set_xlim3d([-radius + root_xyz[0], radius + root_xyz[0]])
    ax.set_ylim3d([-radius + root_xyz[2], radius + root_xyz[2]])
    ax.set_zlim3d([-radius + root_xyz[1], radius + root_xyz[1]])

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


# def visualize_limb(limb: Limb3D, limb_color: str):
#     """
#     Visualizes the limb with the given color and line width.
#     :param img: The original image
#     :param limb: The limb to visualize
#     :param limb_color: The color in which the limb should be displayed
#     :param line_width: The width of the line visualizing the limb
#     :return: The image with the visualized joints
#     """
#
#     return img
#
#
# def __visualize_limb(draw: ImageDraw, limb: Limb2D, limb_color: Color, line_width: int = 4):
#     draw.line((int(limb.joint_from.x), int(limb.joint_from.y), int(limb.joint_to.x), int(limb.joint_to.y)),
#               fill=limb_color.tuple_rgb,
#               width=line_width)



def display_humans(human: Human, plot_labels: bool = False):
    """
    Visualizes all human skeletons and straying joints / limbs in the image and displays the image.
    :param img: The original image
    :param humans: The human content in the image
    :param min_limb_score_to_show: The minimum score of limbs to be displayed
    :param wait_for_ms: The time for which the image should be displayed, if zero wait for keypress
    :return: The image with the visualized humans and straying joints / limbs
    """
    fig = plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(111, projection='3d')
    __init_coordinate_system(ax, [human.skeleton.joints[0].x, human.skeleton.joints[0].y, human.skeleton.joints[0].z])

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

    plt.show()

x = Human()
x.skeleton = pickle.load(open("/media/disks/beta/example_data/skeleton3d.pkl", 'rb'))
a = SkeletonStickman3D
display_humans(x)