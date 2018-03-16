def choose_word(file_path, index):
    """
    The function returns a tuple with the all individuals words in the list and the word in the specified index
    :param file_path: The file path
    :type file_path: str
    :param index: the index of the word in the file (will be -1 afterwards)
    :return: A tuple with the individuals words in the list and the word in the index
    :rtype: tuple
    """
    index -= 1
    with open(file_path, 'r') as f:
        word_list = f.read().split()
    while index >= len(word_list):
        index -= len(word_list)
    return length_no_duplicates(word_list), word_list[index]


def length_no_duplicates(word_list):
    """
    The function checks for the number of words in the world list without duplicates
    :param word_list: The word list
    :type word_list: list
    :return: The length of the list without duplicates
    :rtype: int
    """
    new_list = []
    for item in word_list:
        if item not in new_list:
            new_list.append(item)
    return len(new_list)