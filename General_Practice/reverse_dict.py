def inverse_dict(my_dict):
    """
    The function reverts dictionary order: key are values values are keys. All the values are in a list and sorts the lists
    :param my_dict: the dict to revert
    :type my_dict: dict
    :return: The reversed dict
    :rtype: dict
    """
    new_dict = {}
    for item in my_dict:
        if my_dict[item] not in new_dict:
            new_dict[my_dict[item]] = [item]
        else:
            new_dict[my_dict[item]].append(item)
            new_dict[my_dict[item]].sort()

    return new_dict

