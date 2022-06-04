arr = [[1,0,1,0,1], [1,1,0,0,0], [0,1,0,1,1]]
for i in arr:
    for j in i:
        print(str(j)+" ", end="")
    print()

visited_arr = [[False for i in range(5)] for j in range(3)]
count = 0
for i in range(0,len(arr)):
    for j in range(0,len(arr[0])):
        if arr[i][j] == 1 and visited_arr[i][j] == False:
            count += 1


