# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106


from functools import reduce
a = input()
total, tmp = 0, str()
for i in range(4):
    tmp += a
    total += int(tmp)
print(total)


a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)
print(total)

x = input('please enter a digit:')
reduce(lambda x, y: int(x) + int(y), [x*i for i in range(1, 5)])


def question_15(string_digit):
    return sum(int(string_digit * n) for n in range(1, 5))


inp = input()
print(question_15(inp))
