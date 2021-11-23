matrix = [[x for x in range(1+(5*y), 6+(5*y))] for y in range(4)]
print(matrix)

row = len(matrix)
col = len(matrix[0]) - 1

for i in range(row):
    r, c = i, 0
    while r>=0 and c <= col:
        print(matrix[r][c], end=" ")
        r = r - 1
        c = c+ 1
    print()


for i in range(1, col+1):
    r, c = row - 1, i
    while r>=0 and c <= col:
        print(matrix[r][c], end=" ")
        r = r - 1
        c = c + 1
    print()

