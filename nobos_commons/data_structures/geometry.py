class Triangle(object):
    __slots__ = ['a', 'b', 'c', 'alpha_rad', 'beta_rad', 'gamma_rad']

    def __init__(self, a: float, b: float, c: float, alpha_rad: float, beta_rad: float, gamma_rad: float):
        """
        Represents a triangle with radian angles.
        :param a: The a coordinate
        :param b: The b coordinate
        :param c: The c coordinate
        :param alpha_rad: The alpha angle (radians)
        :param beta_rad: The beta angle (radians)
        :param gamma_rad: The gamma angle (radians)
        """
        self.a = a
        self.b = b
        self.c = c
        self.alpha_rad = alpha_rad
        self.beta_rad = beta_rad
        self.gamma_rad = gamma_rad
