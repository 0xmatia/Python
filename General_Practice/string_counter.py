def numbers_letters_count(my_str):
    """
    This function count how many time numbers appears in a string and how many time another chars appear
    :param my_str: a string to check on
    :type my_str: str
    :return: a list with the number of numbers in a string in index 0, and the numbers of other chars in index 1
    :rtype list
    """
    new_list = [0, 0] # initialize the list with zeros so we can ++ later
    for item in my_str:
        if item.isnumeric():
            new_list[0] += 1
        else:
            new_list[1] += 1
    return new_list
