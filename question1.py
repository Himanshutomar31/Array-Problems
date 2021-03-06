# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

# method1
l = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        l.append(str(i))
print(','.join(l))

# method2
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')
print("\b")

# method1
lst = (str(i) for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0)
print(type(lst))
print(','.join(lst))
