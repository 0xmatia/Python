def main():
    pass


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
    strength = ""
    if password.isnumeric():
        strength = 0
    elif password.isalpha():
        strength = 3
    elif password


def has_number(password):
    for digit in password:
        if digit.isnumeric():
            return True
    return False

def has_small_letter(password):

if __name__ == '__main__':
    main()
