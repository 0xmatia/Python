def squared_numbers(start, stop):
    """
    This function returns a list with all the square numbers between start and stop
    :param start: the first variable to start the square
    :type start: int
    :param stop: The last value the fuction checks for squares
    :type stop: int
    :return: a list with all the squares between start and stop
    :rtype: list
    """
    my_list = []
    while start <= stop:
        my_list.append(start * start)
        start += 1
    return my_list


