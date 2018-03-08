def count_chars(my_str):
    """
    The function returns a list with all the letters in the string with their count
    :param my_str: A string
    :type my_str: str
    :return: The dict with the letters and their count
    :rtype: dict
    """
    new_dict = {}
    for item in my_str:
        if (item not in new_dict) and not(item == ' '):
            new_dict[item] = my_str.count(item)
    return new_dict


