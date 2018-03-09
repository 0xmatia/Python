def are_files_equal(file1, file2):
    """
    The function checks if two files are equal
    :param file1: one file
    :type file1: str
    :param file2:  Other file
    :type file2: str
    :return: True if the files are equal, false otherwise
    :rtype: bool
    """
    new_file1 = 0
    new_file2 = 0
    with open(file1, "r") as file1_text:
        new_file1 = file1_text.read()
    with open(file2, "r") as fil2_text:
        new_file2 = fil2_text.read()
    if new_file1 == new_file2:
        return True
    return False

