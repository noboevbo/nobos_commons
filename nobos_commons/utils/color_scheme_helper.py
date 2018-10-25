from typing import List


def get_color_scheme(color_scheme_length: int = 7, channels: int = 3) -> List[List[int]]:
    """
    Returns a color scheme for 1, 2 or 3 channels. The color scheme will return a equal distribution from 0 to 255 for
    each channel.
    :param color_scheme_length: The length of the color scheme
    :param channels: The number of channels of the color scheme
    :return:
    """
    if channels == 1:
        return get_color_scheme_1_channel(color_scheme_length)
    if channels == 2:
        return get_color_scheme_2_channel(color_scheme_length)
    if channels == 3:
        return get_color_scheme_3_channel(color_scheme_length)
    else:
        raise NotImplementedError("color scheme for {0} channels is not implemented".format(channels))


def get_color_scheme_1_channel(color_scheme_length: int) -> List[List[int]]:
    step_size = int(255 / color_scheme_length) # round down
    colors = [[255]]
    for i in range(1, color_scheme_length - 1):
        step_num = i * step_size
        colors.append([255 - step_num])
    colors.append([0])
    return colors


def get_color_scheme_2_channel(color_scheme_length: int) -> List[List[int]]:
    step_size = int(255 / color_scheme_length) # round down
    colors = [[255, 0]]
    for i in range(1, color_scheme_length - 1):
        step_num = i * step_size
        colors.append([255 - step_num, 0 + step_num])
    colors.append([0, 255])
    return colors


def get_color_scheme_3_channel(color_scheme_length: int) -> List[List[int]]:
    """
    Use channel 1, 2 to time_frame_length / 2 and channel 2, 3 for the other half of the time frame
    :param color_scheme_length:
    :return:
    """
    time_frame_split_1 = int(color_scheme_length / 2)
    time_frame_split_2 = color_scheme_length - time_frame_split_1
    split_1_step_size = int(255 / time_frame_split_1)
    split_2_step_size = int(255 / time_frame_split_2)
    colors = [[255, 0, 0]]
    for i in range(1, time_frame_split_1):
        step_num = i * split_1_step_size
        colors.append([255-step_num, 0 + step_num, 0])
    colors.append([0, 255, 0])
    for i in range(1, time_frame_split_2 - 1):
        step_num = i * split_2_step_size
        colors.append([0, 255 - step_num, 0 + step_num])
    colors.append([0, 0, 255])
    return colors