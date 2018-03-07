

def arrow(my_char, max_length):
    """
    The function prints a arrow with the given symbol, max length is max length
    :param my_char: what to print in the arrow
    :type my_char: str
    :param max_length: the total length of the arrow
    :type max_length: int
    :return: A string with the arrow
    :rtype: str
    """
    new_list = []
    for i in range(1, max_length + 2):
        for j in range(1, i):
            new_list.append(my_char)
        new_list.append("\n")
    for i in range(max_length-1, 0, -1):
        for j in range(i, 0, -1):
            new_list.append(my_char)
        new_list.append("\n")
    new_list = "".join(new_list)
    return new_list


print(arrow("*", 5))

