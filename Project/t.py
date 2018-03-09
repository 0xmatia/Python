HANGMAN_PHOTOS = {"stage 1": """
x-------x
"""}

HANGMAN_PHOTOS["stage 2"] = """
x-------x
|
|
|
|
|
"""

HANGMAN_PHOTOS["stage 3"] = """
x-------x
|       |
|       0
|
|
|
"""

HANGMAN_PHOTOS["stage 4"] = """
x-------x
|       |
|       0
|       |
|
|
"""

HANGMAN_PHOTOS["stage 5"] = """
x-------x
|       |
|       0
|      /|\\
|
|
"""

HANGMAN_PHOTOS["stage 6"] = """
x-------x
|       |
|       0
|      /|\\
|      /
|
"""

HANGMAN_PHOTOS["stage 7"] = """
x-------x
|       |
|       0
|      /|\\
|      / \\
|"""


def print_hangman(num_of_tries):
    """
    The function prints the correct hangman picture by given current turn.
    :param num_of_tries: the number of failed turns
    :type num_of_tries: int
    :return: None
    """
    print(HANGMAN_PHOTOS["stage "+str(num_of_tries)])


