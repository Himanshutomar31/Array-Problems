def sortArr(arr):
    gap = len(arr)
    n = len(arr)
    swap = True
    while(gap != 1 and swap):
        swap = False
        gap = (int)(gap/1.3)
        for i in range(0,n-gap):
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                swap = True
    return arr


arr = [50, 10, 25, -45, 30, 28]
print(sortArr(arr))
