array = [0, 1, 2, 2, 4, 4, 5, 5, 5, 8]
key = 5


def first_index(arr, key, low, high):
    if low > high:
        return -1

    if low == high:
        return low

    mid = int((low+high)/2)

    if mid < high and arr[mid] == key and arr[mid-1] < arr[mid]:
        return mid

    if arr[mid] < key:
        return first_index(arr, key, mid+1,high)
    else:
        return first_index(arr,key,low,mid-1)
    pass


print(first_index(array, key,0,len(array)-1))