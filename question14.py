# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

sentence = input()
count1 = 0
count2 = 0
for i in sentence:
    if i.isupper():
        count1 += 1
    if i.islower():
        count2 += 1
print(count1)
print(count2)

s = input()
d = {"UPPER CASE": 0, "LOWER CASE": 0}
for c in s:
    if c.isupper():
        d["UPPER CASE"] += 1
    elif c.islower():
        d["LOWER CASE"] += 1
    else:
        pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])


word = input()
upper, lower = 0, 0

for i in word:
    if 'a' <= i and i <= 'z':
        lower += 1
    if 'A' <= i and i <= 'Z':
        upper += 1

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))


word = input()
upper, lower = 0, 0

for i in word:
    lower += i.islower()
    upper += i.isupper()

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))
