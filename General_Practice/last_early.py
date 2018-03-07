def last_early(my_str):
    last_letter = my_str[len(my_str) - 1]
    my_str = my_str.lower()
    if last_letter in my_str[:len(my_str) - 1]:
        return True
    else:
        return False


