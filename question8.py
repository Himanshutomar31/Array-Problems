# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

lst = input().split(",")
lst.sort()
print(','.join(lst))


# let's sort it by third char
def my_func(e):
    return e[2]


my_list = input('Enter a comma separated string: ').split(",")
my_list.sort(key=my_func)
print(",".join(my_list))
