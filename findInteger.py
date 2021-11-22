arr1 = [5, 5, 4, 8, 4, 5, 8, 9, 4, 8]

def find_Element(arr1):
    d = {}
    for i in arr1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in arr1:
        if d[i] == 1:
            return i

    return -1



print(find_Element(arr1))
