def seven_boom(end_number):
    """
    This function plays seven boon until end number
    :param end_number: how far to play
    :type end_number: int
    :return: a list with number and boom where a number contains 7 or is dividable by 7
    :rtype: list
    """
    SPECIAL = '7'
    NUMBER = 7
    my_list = []
    for number in range(end_number + 1):
        if (number % NUMBER == 0) or (SPECIAL in str(number)):
            my_list.append("BOOM")
        else:
            my_list.append(number)
    return my_list


print(seven_boom(260))
