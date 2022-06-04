# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:
# 100,150,180 The output of the program should be:18,22,24


from math import sqrt


def calculate(lst):
    res_lst = list()
    C = 50
    H = 30
    for D in lst:
        ans = sqrt((2*C*D)//H)
        res_lst.append(str(round((ans))))
    return ','.join(res_lst)


lst = map(int, input().split(","))
print(calculate(lst))
