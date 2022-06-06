# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are
# divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# 0100,0011,1010,1001
# Then the output should be:
# 1010


def binary_to_decimal(num):
    res = 0
    for i in range(len(num)):
        res += int(num[i]) * 2**i
    return res


def calculate(lst):
    res = []
    for i in lst:
        ans = binary_to_decimal(list(i))
        if ans % 5 == 0:
            res.append(i)
    return ",".join(res)


lst = input().split(",")
print(calculate(lst))


value = []
items = [x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp % 5:
        value.append(p)

print(",".join(value))


def check(x):
    return int(x, 2) % 5 == 0


data = input().split(',')
data = list(filter(check, data))
print(",".join(data))


data = input().split(',')
data = list(filter(lambda i: int(i, 2) % 5 == 0, data))
print(",".join(data))

data = input().split(',')
data = [num for num in data if int(num, 2) % 5 == 0]
print(','.join(data))
