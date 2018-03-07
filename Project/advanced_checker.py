def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function checks if the user entered the input correctly: length of the string is 1, the letter guessed isn't in the old_letters_guessed list, and no special characters
    :param letter_guessed: the input the user entered
    :type letter_guessed int
    :param old_letters_guessed: The list with all the previous guesses
    :type old_letters_guessed: list
    :return: True if the input is valid, false otherwise
    :rtype boolean
    """
    letter_guessed = letter_guessed.lower()
    if (letter_guessed.isalpha()) and (len(letter_guessed) == 1 and (letter_guessed not in old_letters_guessed)):
        return True
    return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    This function checks, update, and print according to user input
    :param letter_guessed: the letter the user guessed
    :type letter_guessed: str
    :param old_letters_guessed: the list with all the old guesses
    :type old_letters_guessed: list
    :return: False if the user input is incorrect, and the old letters with arrows between them sorted, true if the input is correct and adds the guess into the list
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        old_letters_guessed.sort()
        old_letters_guessed = ' -> '.join(old_letters_guessed)
        old_letters_guessed.lower()
        print(old_letters_guessed)
        return False

