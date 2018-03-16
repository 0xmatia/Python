def main():
    MAX_TRIES = 6
    num_of_tries = 0
    old_letters_guessed = []
    print_hangman()
    print(MAX_TRIES)
    # asks for file path:
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    secret_word = choose_word(file_path, index)
    hangman_pics(num_of_tries)
    while not check_win(secret_word, old_letters_guessed):
        print(show_hidden_word(secret_word, old_letters_guessed))
        guess = input("Guess a letter: ")
        while not try_update_letter_guessed(guess, old_letters_guessed):
            guess = input("Guess a letter: ")
        if guess not in secret_word:
            print(":(")
            num_of_tries += 1
            hangman_pics(num_of_tries)
            if num_of_tries == MAX_TRIES:
                print(show_hidden_word(secret_word, old_letters_guessed))
                print("LOSE")
                break
    if check_win(secret_word, old_letters_guessed):
        print(show_hidden_word(secret_word, old_letters_guessed))
        print("WIN")


def print_hangman():
    """
    Prints the welcome screen and max tries for hangman
    :return: NOne
    """

    HANGMAN_ASCII_ART = """
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/
"""
    print(HANGMAN_ASCII_ART)


def choose_word(file_path, index):
    """
    The function returns the word in the specified index
    :param file_path: The file path
    :type file_path: str
    :param index: the index of the word in the file (will be -1 afterwards)
    :return: the word in the index
    :rtype: str
    """
    index -= 1
    with open(file_path, 'r') as f:
        word_list = f.read().split()
    while index >= len(word_list):
        index -= len(word_list)
    return word_list[index]


def hangman_pics(current_guess):
    """
    This function prints the hangman picture according to current_guess
    :param current_guess: The current guess of the player (out of MAX_TRIES)
    :type current_guess:  int
    :return:none
    """
    HANGMAN_PHOTOS = {"stage 0": """x-------x
"""}

    HANGMAN_PHOTOS["stage 1"] = """x-------x
|
|
|
|
|
"""

    HANGMAN_PHOTOS["stage 2"] = """x-------x
|       |
|       0
|
|
|
"""

    HANGMAN_PHOTOS["stage 3"] = """x-------x
|       |
|       0
|       |
|
|
"""

    HANGMAN_PHOTOS["stage 4"] = """x-------x
|       |
|       0
|      /|\\
|
|
"""

    HANGMAN_PHOTOS["stage 5"] = """x-------x
|       |
|       0
|      /|\\
|      /
|
"""

    HANGMAN_PHOTOS["stage 6"] = """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""
    print(HANGMAN_PHOTOS["stage " + str(current_guess)])


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


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function checks if the user entered the input correctly: length of the string is 1, the letter guessed isn't in the old_letters_guessed list, and no special characters
    :param letter_guessed: the input the user entered
    :type letter_guessed str
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


if __name__ == '__main__':
    main()
