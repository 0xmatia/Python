def is_valid_input(letter_guessed):
    """
    This function checks if the user entered the input correctly: length of the string is 1 and no special characters
    :param letter_guessed: the input the user entered
    :type letter_guessed int
    :return: True if the input is valid, false otherwise
    :rtype boolean
    """
    if (letter_guessed.isalpha()) and (len(letter_guessed) == 1):
        return True
    return False


second_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(second_list[1][0][1])
