import math
string = input("Please enter a string: ")
x = math.floor(len(string)/2)
y = math.floor((len(string) - len(string)/2))

first_half = string[:x].lower()
second_half = string[y:].upper()

print(first_half + second_half)
