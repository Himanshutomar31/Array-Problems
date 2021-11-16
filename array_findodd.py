
# O(n) complexity
def find_odd_count(arr):
    d={}
    for i in arr:
        if i not in d:
            d[i] = 1
        else :
            d[i] += 1

    for i in  d:
        if d[i] % 2 != 0:
            return i
    return -1

def find_odd_count2(arr):
    result = arr[0]
    for i in range(1,len(arr)):
        result = result^arr[i]

    return result

arr = [2, 5, 9, 1, 5, 1, 8, 2, 8]
print(find_odd_count2(arr))