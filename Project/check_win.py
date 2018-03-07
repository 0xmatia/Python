def check_win(secret_word, old_letters_guessed):
    """
    This function returns true if the player won the game false otherwise
    :param secret_word: The secret word
    :type secret_word: str
    :param old_letters_guessed: all the letters the user guessed
    :type old_letters_guessed: list
    :return: True if the player won, false otherwise
    :rtype: bool
    """
    length = 0
    for item in secret_word:
        if item in old_letters_guessed:
            length += 1
    if length == len(secret_word):
        return True
    return False


