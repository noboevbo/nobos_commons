class Triangle(object):
    __slots__ = ['a', 'b', 'c', 'alpha_rad', 'beta_rad', 'gamma_rad']

    def __init__(self, a: float, b: float, c: float, alpha_rad: float, beta_rad: float, gamma_rad: float):
        self.a = a
        self.b = b
        self.c = c
        self.alpha_rad = alpha_rad
        self.beta_rad = beta_rad
        self.gamma_rad = gamma_rad
