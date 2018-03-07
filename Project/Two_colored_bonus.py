import termcolor
import colorama

colorama.init()
# State 0

print(termcolor.colored("""
    x-------x
""", "green"))

# State 1

print(termcolor.colored("""
    x-------x
    |
    |
    |
    |
    |
""", "green"))

# State 2
print(termcolor.colored("""
    x-------x
    |       |
    |       0
    |
    |
    |
""", "green"))

# State 3
print(termcolor.colored("""
    x-------x
    |       |
    |       0
    |       |
    |
    |
""", "green"))

# State 4

print(termcolor.colored("""
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""", "green"))

# State 5

print(termcolor.colored("""
     x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""", "green"))

# State 6

print(termcolor.colored("""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""", "green"))
