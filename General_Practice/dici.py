import datetime


def main():
    """
    Main function
    :return: None
    """
    my_dict = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970",
               "hobbies": ["Sing", "Compose", "Act"]}
    menu(my_dict)


def menu(dict):
    """
    Prints the menu and calls varius functions
    :param dict: The dictionery with the details
    :type dict: dict
    :return: None
    :rtype: None
    """
    print("1)\tPrint last name: ")
    print("2)\tPrint Mariah month birth: ")
    print("3)\tPrint how many hobbies Mariah has: ")
    print("4)\tPrint last hobby: ")
    print("5)\tAdd cooking to the hobby list: ")
    print("6)\tChange date format: ")
    print("7)\tAdd age value: ")
    choice = int(input())
    if choice == 1:
        last_name(dict)
    if choice == 2:
        print_month(dict)
    if choice == 3:
        how_many_hobbies(dict)
    if choice == 4:
        last_hobby(dict)
    if choice == 5:
        dict = add_cooking(dict)
    if choice == 6:
        dict = change_date(dict)
    if choice == 7:
        dict = add_age(dict)


def last_name(dict):
    """
    Prints the last name from the dict
    :param dict: The dict with the details
    :type dict: dict
    :return: None
    """
    print(dict["last_name"])


def print_month(dict):
    """
    Prints the the month from the dict
    :param dict: The dict
    :type dict: dict
    :return: None
    """
    date = dict["birth_date"]
    print(date[3:5])


def how_many_hobbies(dict):
    """
    Prints the length of hobbies from the dict
    :param dict: The dict with the details
    :type dict: dict
    :return: None
    """
    hobbies = dict["hobbies"]  # list
    print(len(hobbies))


def last_hobby(dict):
    """
    Print the last hobby in the dictionary
    :param dict: THe dict with details
    :type dict: dict
    :return: None
    """
    hobbies = dict["hobbies"]  # list
    print(hobbies[-1])


def add_cooking(dict):
    """
    The function adds Cooking to hobbies dict
    :param dict: The dict with details
    :type dict: dict
    :return: The updated dict
    :rtype: dict
    """
    hobbies = dict["hobbies"]  # list
    hobbies.append("Cooking")
    dict["hobbies"] = hobbies
    return dict


def change_date(dict):
    """
    The function updates the dict: put tuple instead
    :param dict: The dict with details
    :type dict: dict
    :return: The updated dict
    :rtype: dict
    """
    date = dict["birth_date"]
    new_tuple = (date[0:2], date[3:5], date[6:])
    print(new_tuple)
    dict["birth_date"] = new_tuple
    return dict


def add_age(dict):
    """
    The function adds and print the age of Mariah
    :param dict: The dict with the details
    :type dict: dict
    :return: The updated dict
    :rtype: dict
    """
    now = datetime.datetime.now()
    current_year = now.year
    date = dict["birth_date"]
    age = current_year - int(date[6:])
    dict["age"] = age;
    print(age)
    return dict


if __name__ == '__main__':
    main()
