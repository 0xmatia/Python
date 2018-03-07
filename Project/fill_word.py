def show_hidden_word(secret_word, old_letters_guessed):
    """
    This function returns a string with all the letter guessed in the right spot, and '_' in the missing spots
    :param secret_word: The word the user need to guess
    :type secret_word: str
    :param old_letters_guessed: all the letters that have been already guessed
    :type old_letters_guessed: list
    :return: A string with the correct letter guessed in their spot, and _ where the letter were'nt guessed
    :rtype: str
    """
    new_string = ""
    for item in secret_word:
        if item in old_letters_guessed:
            new_string += item
            new_string += " "
        else:
            new_string += "_ "
    new_string = new_string.rstrip()
    # new_list = "".join(new_list)
    return new_string

