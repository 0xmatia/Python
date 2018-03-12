import re


def main():
    path = input("Enter a file path: ")
    task = input("Enter a task: ")
    if task == "sort":
        sort(path)
    elif task == "rev":
        rev(path)
    elif task == "last":
        print_line(path)


def put_in_list(path):
    """
    Helper function for sort() which put the text from a given path into a file
    :param path: The path to the file
    :type path: str
    :return: A list with the text file
    :rtype: list
    """
    string = ""
    new_list = []
    no_duplicate = []
    with open(path, "r") as text_file:
        string = text_file.read()
    new_list = string.split()
    for item in new_list:
        if item not in no_duplicate and (not item == ''):
            no_duplicate.append(item)
    return no_duplicate


def rev(path):
    """
    The function prints the text file backwards
    :param path: The path to the file
    :type path: str
    :return: None
    """
    list = open(path).readlines()
    new_list = []
    another_list = []
    index1 = 0
    index2 = 0
    final_string = ""
    for line in list:
        new_list.append(re.sub("[^\w]", " ", line).split())  # -> taken from stack overflow! <-
    # reverse the rows
    for line in new_list:
        a = line[::-1]
        another_list.append(a)

    # revert all the words in the list
    for line in another_list:
        for word in line:
            another_list[index1][index2] = word[::-1]
            index2 += 1
        index2 = 0
        index1 += 1
    for line in another_list:
        for word in line:
            final_string = final_string + " " + word
    final_string.lstrip()
    final_string = final_string[1:]  # removes the first space (duuno why it even creates)
    print(final_string)


def print_line(path):
    """
    The function prints lines from n to the end
    :param path: The path to the file
    :type path: str
    :return: None
    """
    n = int(input("Enter a number: "))
    with open(path, "r") as text_file:
        for i in enumerate(text_file):
            if int(i[0]) >= n:
                a = "".join(i[1:])
                print(a)


def sort(path):
    """
    The function sort the list from the file
    :param path: The path to the file
    :type path: str
    :return: None
    """
    word_list = put_in_list(path)
    word_list.sort()
    print(word_list)


if __name__ == '__main__':
    main()
