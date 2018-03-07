def main():
    string = input("Enter your groceries: ")
    string = string.replace(',', " ", len(string))
    string = string.split()
    menu(string)


def menu(g_list):
    """
    Prints the menu for the user
    :param g_list: the list the user entered converted from a string
    :type g_list: list
    :return: None
    """
    choice = 0
    while not choice == 9:
        print("\n\n1)\tPrint the groceries")
        print("2)\tPrint the length of the grocery list")
        print("3)\tFind out if something is in the grocery list")
        print("4)\tFind out how many times X is in the list")
        print("5)\tRemove item from the list")
        print("6)\tAdd item to the list")
        print("7)\tPrint illegal groceries")
        print("8)\tRemove duplicates")
        print("9)\tExit")
        choice = int(input())
        if choice == 1:
            print_grocery(g_list)
        elif choice == 2:
            g_length(g_list)
            pass
        elif choice == 3:
            print(is_on_list(g_list))
        elif choice == 4:
            print(count_occurance(g_list))
        elif choice == 5:
            g_list = remove(g_list)
        elif choice == 6:
            g_list = add(g_list)
        elif choice == 7:
            print_illegal(g_list)
        elif choice == 8:
            g_list = remove_duplicate(g_list)
        elif choice == 9:
            # exit
            pass


def print_grocery(grocery):
    """
    Prints the list
    :param grocery: the list to print
    :type grocery: list
    :return: None
    """
    grocery = ", ".join(grocery)
    print(grocery)


def g_length(g_list):
    """
    Returns the list's length
    :param g_list: the list
    :type g_list: list
    :return: None
    """
    print(len(g_list))


def is_on_list(g_list):
    """
    Checks if something is in the list
    :param g_list: the list to check if something is in it
    :type g_list: list
    :return: None
    """
    grocery = input("What do you wish to check in the list? ")
    if grocery in g_list:
        # print("\'" + grocery + "\'" + " is in the list")
        return True
    else:
        # print("\'" + grocery + "\'" + " is not in the list")
        return False


def count_occurance(g_list):
    """
    Checks how many times a string apears in the list
    :param g_list: the list to check how many times apears in it
    :type g_list list
    :return: None
    """
    g = input("Enter a grocery: ")
    count = 0
    for string in g_list:
        if string == g:
            count += 1
    print("The number of times \'" + g + "\' apears in the list: " + str(count))


def remove(g_list):
    """
    Removes item from the list
    :param g_list: the list to remove item from
    :type g_list: list
    :return: None
    """
    g = input("Enter the item you wish to remove: ")
    g_list.remove(g)
    return g_list


def add(g_list):
    """
    The function adds item to the list
    :param g_list:
    :return:
    """
    g = input("Enter an item you wish to add: ")
    g_list.append(g)
    return g_list


def print_illegal(g_list):
    """
    The function returns a string with all the illegal groceries (len less then 3 and not alphabet)
    :param g_list: The list with the groceries
    :type g_list: list
    :return: None
    :rtype: None
    """
    illegal = []
    for item in g_list:
        if (len(item) < 3) or not (item.isalpha()):
            illegal.append(item)
    illegal = " ".join(illegal)
    print(illegal)


def remove_duplicate(g_list):
    """
    Remove duplicate items in the grocery list
    :param g_list: The grocery list
    :type g_list: list
    :return: The updated list
    :rtype: str
    """
    new_list = []
    for item in g_list:
        if item not in new_list:
            new_list.append(item)
    return new_list


if __name__ == '__main__':
    main()
