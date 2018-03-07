def mult_tuple(tuple1, tuple2):
    """
    The function returns a tuple with all the possible coordinated given with the tuples
    :param tuple1: The first tuple with x and y
    :type tuple1: tuple
    :param tuple2: The second tuple with X and Y
    :type tuple2: tuple
    :return: A tuple with all the possible coordinated with the given points
    :rtype: tuple
    """
    new_tuple = ()
    # go through the first tuple first
    for item in tuple1:
        for another_item in tuple2:
            # We need these items to be deleted after every iteration
            b = (item, another_item)
            c = (another_item, item)
            new_tuple += (b, c,)
    return new_tuple
