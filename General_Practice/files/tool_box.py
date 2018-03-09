import re


def main():
    path = input("Enter a file path: ")
    task = input("Enter a task: ")
    if task == "sort":
        sort(path)


def sort(path):
    string = ""
    with open(path, "r") as text_file:
        string = text_file.read()
    wordList = re.sub("[^\w]", " ", string).split()  # -> taken from stack overflow! <-
    wordList.sort()
    print(wordList)


if __name__ == '__main__':
    main()
