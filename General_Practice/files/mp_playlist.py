def my_mp3_playlist(file_path):
    """
    This function returns a tuple with the longest song time, the numbers of rows in the file and the most popular author in a rile
    :param file_path: The path to the file with songs
    :type file_path: str
    :return: A tuple with the relevant information
    :rtype: tuples
    """
    each_row = []
    with open(file_path, "r") as text_file:
        # puts the text file in a text
        playlist = text_file.read()
    playlist = playlist.split('\n')  # puts each row in its place
    for song in playlist:
        song = song.split(';')  # make each part an item
        song = song[:-1]  # removes the last semicolon (blank)
        each_row.append(song)
    # check if a new line is present and deletes it
    if not each_row[-1]:
        each_row = each_row[:-1]

    return longest_song(each_row), len(each_row), common_author(each_row)


def longest_song(song_list):
    """
    Returns the longest time of a song in the file
    :param song_list: The list with all the songs details
    :type song_list: list
    :return: The name of the maximum  length song
    :rtype: str
    """
    time_list = []
    name_list = []
    correct_lengths = []
    time_dict = {}
    longest = ""
    max_len = 0.0
    # creates two list, one with the names the other with the lengths
    for song in song_list:
        time_list.append(song[2])
        name_list.append(song[0])
    for length in time_list:
        length = length.replace(":", ".")  # replace : with . so we can do calculation on it
        correct_lengths.append(length)
    # creates a dictionary with name: length
    for k in range(len(time_list)):
        time_dict[name_list[k]] = correct_lengths[k]
    # find out what is the longest song
    for key, value in time_dict.items():
        if float(value) > max_len:
            max_len = float(value)
            longest = key
    return longest


def common_author(song_list):
    """
    This function finds the most common author in a list
    :param song_list: A list with all the songs
    :type song_list: list
    :return: The most common author
    :rtype: str
    """
    author_list = []
    author_dict = {}
    author_common = ""
    max_appearances = 0
    # puts all the authors in a list
    for author in song_list:
        author_list.append(author[1])
    # counts the number of times each author is appearing in the list and puts it in a dictionary
    for author in author_list:
        if author not in author_dict:
            author_dict[author] = 1
        else:
            author_dict[author] += 1
    # checks for the most common author and returns it
    for key, value in author_dict.items():
        if value > max_appearances:
            max_appearances = value
            author_common = key
    return author_common
