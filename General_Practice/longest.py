def longest(my_list):
    """
    This function returns the longest string in a given list
    :param my_list: The list to check for the longest string
    :type my_list: list
    :return: The longest string in the given list
    :rtype: str
    """
    return max(my_list, key=len)


list1 = ["111", "234", "2000", "goru", "birthday", "09"]
print(longest(list1))
