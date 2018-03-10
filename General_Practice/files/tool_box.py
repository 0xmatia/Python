import re


def main():
    path = input("Enter a file path: ")
    task = input("Enter a task: ")
    read_line(path)
    if task == "sort":
        sort(path)
    elif task == "rev":
        rev(path)


def put_in_list(path):
    string = ""
    new_list = []
    no_duplicate = []
    with open(path, "r") as text_file:
        string = text_file.read()
    new_list = re.sub("[^\w]", " ", string).split()  # -> taken from stack overflow! <-
    for item in new_list:
        if item not in no_duplicate:
            no_duplicate.append(item)
    return no_duplicate


def rev(path):
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
        final_string = final_string + '\n'
    final_string.lstrip()
    print(final_string)


def sort(path):
    word_list = put_in_list(path)
    word_list.sort()
    print(word_list)


def rev(path):
    my_list = put_in_list(path)  # get all the words separated in a list
    new_list = []
    for item in my_list:
        new_list.append(item[::-1])
    new_string = " ".join(new_list)
    print(new_string)


if __name__ == '__main__':
    main()
