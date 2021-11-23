matrix = [[1, 1, 0, 0, 1, 1],
          [0, 0, 1, 0, 1, 1],
          [1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 1, 1]]

l = len(matrix)
b = len(matrix[0])
table = []
table = [[0 for x in range(b)] for x in range(l)]
print(table)

for i in range(0,l):
    for j in range(0,b):
        if i == 0 or j == 0:
            table[i][j] = matrix[i][j]

ele = 0
for i in range(1,l):
    for j in range(1, b):
        if matrix[i][j] != 0:
            tmp1 = table[i-1][j]
            tmp2 = table[i][j-1]
            tmp3 = table[i-1][j-1]
            table[i][j] = min(tmp1, tmp2, tmp3) + 1
            if table[i][j] > ele:
                ele = table[i][j]
        else:
            table[i][j] = 0

print(ele)




