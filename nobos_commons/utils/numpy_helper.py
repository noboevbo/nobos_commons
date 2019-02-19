import numpy as np


def set_or_vstack(a: np.ndarray, b: np.ndarray):
    """
    If a exists it vstacks b, if not it sets a to b.
    :param a:
    :param b:
    :return:
    """
    if a is None:
        return b
    else:
        return np.vstack((a, b))

