# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.Suppose the following input
# is supplied to the program: 8 Then, the output should be:40320


# def factorial(n):
#     if n == 1 or n == 0:
#         return n
#     return n * factorial(n-1)

# print(factorial(8))


# n = int(input())
# def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
# print(shortFact(n))


from functools import reduce


def fun(acc, item):
    return acc*item


num = int(input())
print(reduce(fun, range(1, num+1), 1))
