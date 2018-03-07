import termcolor
import colorama

colorama.init()
#State 0

print("""
    x-------x
""")

#State 1

print("""
    x-------x
    |
    |
    |
    |
    |
""")

#State 2
print("""
    x-------x
    |       |
    |       0
    |
    |
    |
""")


#State 3
print("""
    x-------x
    |       |
    |       0
    |       |
    |
    |
""")

#State 4

print("""
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""")

#State 5

print("""
     x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""")

#State 6

print (termcolor.colored("""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""", "green"))
