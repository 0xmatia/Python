def who_is_missing(file_name):
    max = 0
    number = 1
    string = 0
    missing = 0
    with open(file_name, "r  ") as text_file:
        string = text_file.read()
    # find max
    for item in string:
        if item > max:
            max = item

    for item in range(max + 1):
        if number not in string:
            missing = number
            break
        else:
            number += 1
