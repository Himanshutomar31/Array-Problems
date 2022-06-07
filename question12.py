# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is
# an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.


def check_even(i):
    check = True
    while i > 0:
        num = i % 10
        if num % 2 != 0:
            check = False
            break
        i = i // 10
    return check


res = []
for i in range(1000, 3001):
    if check_even(i):
        res.append(str(i))

print(','.join(res))


lst = []

for i in range(1000, 3001):
    flag = 1
    for j in str(i):
        if ord(j) % 2 != 0:
            flag = 0
    if flag == 1:
        lst.append(str(i))

print(",".join(lst))


def check(element):
    return all(ord(i) % 2 == 0 for i in element)


lst = [str(i) for i in range(1000, 3001)]
lst = list(filter(check, lst))
print(",".join(lst))

lst = [str(i) for i in range(1000, 3001)]
lst = list(filter(lambda i: all(ord(j) % 2 == 0 for j in i), lst))
print(",".join(lst))
