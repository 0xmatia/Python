import termcolor

HANGMAN_PHOTOS = {"stage 0": termcolor.colored("""
x-------x
""", "green")}

HANGMAN_PHOTOS["stage 1"] = termcolor.colored("""
x-------x
|
|
|
|
|
""", "green")

HANGMAN_PHOTOS["stage 2"] = termcolor.colored("""
x-------x
|       |
|       0
|
|
|
""", "green")

HANGMAN_PHOTOS["stage 3"] = termcolor.colored("""
x-------x
|       |
|       0
|       |
|
|
""", "green")

HANGMAN_PHOTOS["stage 4"] = termcolor.colored("""
x-------x
|       |
|       0
|      /|\\
|
|
""", "green")

HANGMAN_PHOTOS["stage 5"] = termcolor.colored("""
x-------x
|       |
|       0
|      /|\\
|      /
|
""", "green")

HANGMAN_PHOTOS["stage 6"] = termcolor.colored("""
x-------x
|       |
|       0
|      /|\\
|      / \\
|""", "green")


def print_hangman(num_of_tries):
    """
    The function prints the correct hangman picture by given current turn.
    :param num_of_tries: the number of failed turns
    :type num_of_tries: int
    :return: None
    """
    print(HANGMAN_PHOTOS["stage "+str(num_of_tries)])


print_hangman(5)
