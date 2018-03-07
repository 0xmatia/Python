def shift_left(my_list):
    temp_variable = my_list[0]
    my_list[0] = my_list[1]
    my_list[1] = my_list[2]
    my_list[2] = temp_variable
    return my_list


programming_languages = ['Python', 'Perl', 'R', 'Ruby']

print(programming_languages[3])
