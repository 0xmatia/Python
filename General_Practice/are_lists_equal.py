def are_lists_equal(list1, list2):
    """
    This functions checks if two lists are identical (not necessary the right order)
    :param list1: one list to compare
    :type list1: list
    :param list2: another list to compare
    :type list2: list
    :return: True if the lists are identical, false otherwise
    :rtype: bool
    """
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False

