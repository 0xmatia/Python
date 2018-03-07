def sequence_del(my_str):
    """
    this function deletes duplicate letters in a given string
    :param my_str: the given string to delete everything duplicate
    :type my_str: str
    :return: A list with no duplicate
    :rtype: list
    """
    new_list = []
    for char in my_str:
        if char not in new_list:
            new_list.append(char)
    new_list = "".join(new_list)
    return new_list


