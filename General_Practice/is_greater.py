def is_greater(my_list, n):
    """
    This function returns a list with all the numbers that are greater than n
    :param my_list: A list with numbers
    :type my_list: list
    :param n: all the numbers in the new list have to be greater than n
    :type n: int
    :return: A list with all the items that are greater than n
    :rtype: list
    """
    new_list = []
    for item in my_list:
        if item > n:
            new_list.append(item)
    return new_list


