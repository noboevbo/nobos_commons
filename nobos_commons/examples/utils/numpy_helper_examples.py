import numpy as np

from nobos_commons.utils.numpy_helper import split_numpy_array, split_numpy_array_stepwise

if __name__ == "__main__":
    array_a = np.array(list(range(0, 64)))
    array_b = np.array(list(range(0, 40)))
    array_c = np.array(list(range(0, 32)))
    array_d = np.array(list(range(0, 10)))

    test_1 = list(split_numpy_array(array_a, 32, fill_value=0))
    test_2 = list(split_numpy_array(array_b, 32, fill_value=0))
    test_3 = list(split_numpy_array(array_c, 32, fill_value=0))
    test_4 = list(split_numpy_array(array_d, 32, fill_value=0))

    test_5 = list(split_numpy_array_stepwise(array_a, 32, 1, fill_value=0))
    test_6 = list(split_numpy_array_stepwise(array_b, 32, 1, fill_value=0))
    test_7 = list(split_numpy_array_stepwise(array_c, 32, 1, fill_value=0))
    test_8 = list(split_numpy_array_stepwise(array_d, 32, 1, fill_value=0))
    a = 1

