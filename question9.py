# Write a program that accepts sequence of lines as input and prints the lines after
# making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

lst = list()
while(True):
    n = input("Please enter a string or X to exit")
    if n.upper() == "X":
        print("\n".join(lst))
        break
    else:
        lst.append(n.upper())


def user_input():
    while True:
        s = input()
        if not s:
            return
        yield s


def inputs():
    while True:
        string = input()
        if not string:
            return
        yield string


print(*(line.upper() for line in inputs()), sep='\n')

for line in map(str.upper, user_input()):
    print(line)
