# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# Suppose the following input is supplied to the program:
# 14
# Then, the output should be:
# 0
# 7
# 14

class Generator:
    def seven(self, n):
        for i in range(0, n+1):
            if i % 7 == 0:
                yield i


g = Generator()
for i in g.seven(14):
    print(i)
