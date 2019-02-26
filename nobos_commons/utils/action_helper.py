from nobos_commons.data_structures.humans_metadata.action import Action


def get_action_from_string_start(input_str: str):
    """
    Returns a action from the start of a string, e.g. wave003mcp -> WAVE, walk051mcp -> WALK
    :param input_str:
    :return:
    """
    input_str_tmp = input_str.lower()
    found_actions = []
    for action in Action:
        if input_str_tmp.startswith(action.name.lower()):
            found_actions.append(action)

    actual_action_name = ""
    for action in found_actions:
        if len(action.name) > len(actual_action_name):
            actual_action_name = action.name

    if not actual_action_name:
        raise KeyError("Could not find a adequate action for string start of '{}'".format(input_str))

    return Action[actual_action_name]


def get_action_from_string(input_str: str):
    """
    Returns a action from the start of a string, e.g. wave003mcp -> WAVE, walk051mcp -> WALK
    :param input_str:
    :return:
    """
    input_str_tmp = input_str.lower()
    found_actions = []
    for action in Action:
        if action.name.lower() in input_str_tmp:
            found_actions.append(action)

    actual_action_name = ""
    for action in found_actions:
        if len(action.name) > len(actual_action_name):
            actual_action_name = action.name

    if not actual_action_name:
        raise KeyError("Could not find a adequate action for string '{}'".format(input_str))

    return Action[actual_action_name]
