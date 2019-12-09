import matplotlib.pyplot as plt

from nobos_commons.data_structures.human import Human
from nobos_commons.data_structures.skeletons.skeleton_stickman_3d import SkeletonStickman3D


def display_humans(human: Human, wait_for_ms: int = 0, min_limb_score_to_show: float = 0.4):
    """
    Visualizes all human skeletons and straying joints / limbs in the image and displays the image.
    :param img: The original image
    :param humans: The human content in the image
    :param min_limb_score_to_show: The minimum score of limbs to be displayed
    :param wait_for_ms: The time for which the image should be displayed, if zero wait for keypress
    :return: The image with the visualized humans and straying joints / limbs
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    RADIUS = 750  # space around the subject
    xroot, yroot, zroot = human.skeleton.joints[0].x, human.skeleton.joints[0].y, human.skeleton.joints[0].z
    ax.set_xlim3d([-RADIUS + xroot, RADIUS + xroot])
    ax.set_zlim3d([-RADIUS + zroot, RADIUS + zroot])
    ax.set_ylim3d([-RADIUS + yroot, RADIUS + yroot])

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    # Get rid of the ticks and tick labels
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    ax.get_xaxis().set_ticklabels([])
    ax.get_yaxis().set_ticklabels([])
    ax.set_zticklabels([])
    # ax.set_aspect('equal')

    # Get rid of the panes (actually, make them white)
    white = (1.0, 1.0, 1.0, 0.0)
    ax.w_xaxis.set_pane_color(white)
    ax.w_yaxis.set_pane_color(white)
    # Keep z pane

    # Get rid of the lines in 3d
    ax.w_xaxis.line.set_color(white)
    ax.w_yaxis.line.set_color(white)
    ax.w_zaxis.line.set_color(white)

    plt.show()

x = Human()
x.skeleton = SkeletonStickman3D()
display_humans(x)