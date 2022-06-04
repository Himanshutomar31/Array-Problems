# With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

def generate_dict(n):
    d = dict()
    for i in range(1, n+1):
        d[i] = i*i
    return d


n = int(input())
print(generate_dict(n))


# Using dictionary comprehension
d = {i: i*i for i in range(1, n+1)}
print(d)
