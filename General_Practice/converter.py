temp = input("Insert the temperature you would like to convert: ")
letter = temp[len(temp) - 1]  # f or c
temp = temp[:len(temp) - 1]  # removes the letter
temp = float(temp)  # converts to int

if (letter == 'c') or (letter == 'C'):
    print(str((9 * temp + (32 * 5)) / 5) + 'F')
elif (letter == 'f') or (letter == 'F'):
    print(str((5 * temp - 160) / 9) + 'C')
