def format_list(my_list):
    """
    This function formats the list: prints only the values in the even indexes and adds 'and' between the last two words
    :param my_list: The list to format
    :type my_list: list
    :return the formatted list.
    :rtype: list
    """
    another_string = my_list[::2]
    another_string = ', '.join(another_string)+', '
    last_word = my_list[len(my_list)-1]
    another_string = another_string + 'and ' + last_word
    return another_string
