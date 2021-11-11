def findPivot(arr, low, high):
    if low > high:
        return -1
    if low == high:
        return low

    mid = int((low+high)/2)
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    if mid > low and arr[mid] < arr[mid-1]:
        return mid-1

    if arr[mid] < arr[low]:
        return findPivot(arr,low,mid-1)
    else:
        return findPivot(arr,mid+1,high)


def binarySearch(arr, low, high, key):
    if low > high:
        return -1

    mid = int((low+high)/2)
    if arr[mid] == key:
        return mid
    if arr[mid] > arr[low]:
        return binarySearch(arr,mid+1,high,key)
    else:
        return binarySearch(arr,low,mid-1,key)





def pivotedBinarySearch(arr, l, key):
    pivot = findPivot(arr,0,l-1)
    result = binarySearch(arr,0,pivot,key)
    if result != -1:
        return result
    else:
        return binarySearch(arr,pivot+1,l,key)




arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
n = len(arr1)
key = 3
print("Index of the element is : ",
      pivotedBinarySearch(arr1, n, key))