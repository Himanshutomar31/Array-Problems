# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


from functools import reduce
import re
inp = input()
count1 = 0
count2 = 0
for i in inp:
    if i.isdigit():
        count1 += 1
    elif i.isalpha():
        count2 += 1
print(count1)
print(count2)

word = input()
letter, digit = 0, 0

for i in word:
    if i.isalpha():
        letter += 1
    elif i.isnumeric():
        digit += 1
print(f"LETTERS {letter}\n{digit}")


input_string = input('> ')
print()
counter = {"LETTERS": len(re.findall(
    "[a-zA-Z]", input_string)), "NUMBERS": len(re.findall("[0-9]", input_string))}
print(counter)


sen = input("").split(" ")
alp, digit = 0, 0
for item in sen:
    lst = [char for char in item]
    for j in lst:
        if 64 < ord(j) < 123:
            alp += 1
        if j.isdigit():
            digit += 1
print(f"LETTERS : {alp} \n DIGITS : {digit}")


def count_letters_digits(counters, char_to_check):
    counters[0] += char_to_check.isalpha()
    counters[1] += char_to_check.isnumeric()
    return counters


print('LETTERS {0}\nDIGITS {1}'.format(
    *reduce(count_letters_digits, input(), [0, 0])))
