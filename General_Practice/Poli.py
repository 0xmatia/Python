
s = input("Enter a word: ").lower()
s = s.replace(" ", "") #removes all spaces

if s == s[::-1]:
    print("OK")
else:
    print("NOT")
