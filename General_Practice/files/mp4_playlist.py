def my_mp4_playlist(file_path, new_song):
    each_row = []
    s =  ""
    with open(file_path, "r+") as text_file:
        # puts the text file in a text
        playlist = text_file.read()
    playlist = playlist.split('\n')  # puts each row in its place
    for song in playlist:
        song = song.split(';')  # make each part an item
        song = song[:-1]  # removes the last semicolon (blank)
        each_row.append(song)
    if not each_row[-1]:
        each_row = each_row[:-1]
    # update the list
    if len(each_row) < 3:
        with open(file_path, "a+") as f:
            while len(each_row) < 3:
                f.write("\n")
                each_row.append(f.readlines())
    if not each_row[2]:
        each_row[2] = [new_song]
    else:
        each_row[2][0] = new_song
    # write changes back
    for item in each_row:
        for thing in item:
            s = s + thing+";"
        s += "\n"
    s = s[:-1]  # removes the last newline
    # write
    with open(file_path, "w") as f:
        f.write(s)
    print(s)
