from typing import List

from nobos_commons.data_structures.color import Color
from nobos_commons.data_structures.skeletons.limb_2d import Limb2D


def limb_should_be_displayed(limb: Limb2D, limb_colors: List[Color], min_limb_score_to_show):
    if not limb.is_set:
        return False
    if limb_colors[limb.num] is None:
        return False
    if limb.matched_score < min_limb_score_to_show:
        return False
    return True