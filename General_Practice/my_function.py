def main():
    help(func)


def func(num1, num2):
    """
    This function calculates the distance between num1 and num2
    :param num1: One of the numbers
    :type num2 int
    :param num2: the other number
    :type num1 int
    :return: The absolute value between the two numbers
    :rtype int
    """
    return abs(num1 - num2)


if __name__ == '__main__':
    main()
