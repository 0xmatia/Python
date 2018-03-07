sentence = input("Please enter a string: ")
REPLACE = 'e'
first_letter = sentence[0]
new_sentence = sentence[1:]
print(first_letter + new_sentence.replace(first_letter, REPLACE))

