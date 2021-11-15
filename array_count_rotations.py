arr = [7, 9, 11, 12, 5]


def find_pivot(arr, low, high):
    if low > high:
        return -1
    if low == high:
        return low
    mid = int((low+high)/2)
    if mid < high  and arr[mid] > arr[mid+1]:
        return  mid
    if mid > low and arr[mid-1] > arr[mid]:
        return mid - 1
    if arr[mid] < arr[low]:
        return find_pivot(arr, low, mid-1)
    else:
        return find_pivot(arr, mid+1, high)



# O(n)
def no_of_rotation(arr):
    index = find_pivot(arr, 0, len(arr)-1)
    return index + 1


print(no_of_rotation(arr))