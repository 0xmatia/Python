def who_is_missing(file_name):
    """
    The function finds a missing number in a sequence of number between 1 and n, and writes it to the file
    :param file_name: the path to the file
    :type file_name: str
    :return: The missing number
    :rtype: int
    """
    max = 0
    number = 1
    string = 0
    missing = 0
    with open(file_name, "r") as text_file:
        string = text_file.read()
    # find max
    for item in string:
        if item > str(max):
            max = item

    for item in range(int(max) + 1):
        if str(number) not in string:
            missing = number
            break
        else:
            number += 1
    string = string[:-1]
    with open(file_name, "w") as text_file:
        text_file.write(string + "," + str(missing))
    return missing

