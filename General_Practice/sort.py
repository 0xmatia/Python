def sort_prices(list_of_tuples):
    """
    This function sorts a list of tuples according to the second index of the tuple
    :param list_of_tuples: The list of tuples
    :type list_of_tuples: list
    :return: A list of tuples sorted from the highest price to the lowest
    :rtype: list
    """
    list_of_tuples.sort(key=extract_second, reverse=True)
    return list_of_tuples


def extract_second(item):
    """
    This function is a key function, which return 1 for each item sorted is asking
    :param item: the sort function sends a request and asking according to what to sort in this tuple
    :type item: tuple
    :return: the second item in the tuple (index 1)
    :rtype: tuple - depends on what was in the tuple
    """
    return item[1]




