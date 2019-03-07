from nobos_commons.utils.list_helper import get_chunks_by_list_sampler, split_list, split_list_stepwise

if __name__ == "__main__":
    list_a = list(range(0, 128))
    list_b = list(range(0, 40))
    list_c = list(range(0, 32))
    list_d = list(range(0, 10))

    test_1 = get_chunks_by_list_sampler(list_a, 32, 2)
    test_2 = get_chunks_by_list_sampler(list_b, 32)
    test_3 = list(split_list(list_a, 32))
    test_4 = list(split_list(list_b, 32, 0))

    test_5 = split_list_stepwise(list_a, 32, step_size=3, fill_value=0, every_n_element=2)
    test_6 = split_list_stepwise(list_b, 32, 1, fill_value=0)
    test_7 = split_list_stepwise(list_c, 32, 1, fill_value=0)
    test_8 = split_list_stepwise(list_d, 32, 1, fill_value=0)
    a = 1
