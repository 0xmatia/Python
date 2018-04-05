def main():
    password = input("Please enter a password: ")
    score = int((len_strength(password) + diversity(password) + common_words(password))/3)
    if 0 <= score <= 4:
        print("Score: " + str(score) + " - Weak")
    elif 4 <= score <= 6:
        print("Score: " + str(score) + " - Medium")
    elif 7 <= score <= 8:
        print("Score: " + str(score) + " - Strong")
    elif 9 <= score <= 10:
        print("Score: " + str(score) + " - Very Strong")


def len_strength(password):
    """
    The function checks the password strength. Length between 0 and 4 is 0, length between 5 and 7 is 5, and length higher than 7 is 10
    :param password: The password
    :type password: str
    :return: The strength of the password
    :rtype: int
    """
    strength = 0
    if len(password) < 4:
        strength = 0
    elif 5 <= len(password) <= 7:
        strength = 5
    elif len(password) > 7:
        strength = 10
    return strength


def diversity(password):
    """
    Checks the diversity of the passwords
    :param password:  The password
    :type password: str
    :return: The password strength
    :rtype: int
    """
    if password.isnumeric():
        strength = 0
    elif password.isalpha():
        strength = 3
    elif nums(password) and small_letters(password) and capital_letters(password):
        strength = 7
    elif nums(password) and small_letters(password):
        strength = 5
    else:
        strength = 10
    return strength


def common_words(password):
    """
    Checks to see if the passwords contain no common words
    :param password: The password
    :type password: str
    :return:0 if the the password contain common words
    """
    weak_words = ['abc, qwerty', 'love']
    if password.startswith('password'):
        return 0
    else:
        for item in weak_words:
            if item in password:
                return 0
    return 10


def nums(password):
    """
    Checks if the password has at least one number
    :param password: the password
    :type password: str
    :return: if the password has number
    :rtype: bool
    """
    return any(char.isdigit() for char in password)


def small_letters(password):
    """
    Checks if the password has at least one small letter
    :param password: the password
    :type password: str
    :return: if the password has a small letter in it
    :rtype: bool
    """
    return any(x.islower() for x in password)


def capital_letters(password):
    """    Checks if the password has at least one capital letter
    :param password: the password
    :type password: str
    :return: if the password has one capital letter
    :rtype: bool"""
    return any(x.isupper() for x in password)


if __name__ == '__main__':
    main()
