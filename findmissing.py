arr1 = [9, 7, 8, 5, 4, 6, 2, 3, 1]
arr2 = [2, 4, 3, 9, 1, 8, 5, 6]

def find_Missing_Element(arr1, arr2):
    s1 = set(arr1) # O(N)
    s2 = set(arr2)
    return s1.difference(s2)

def find_Missing_Element2(arr1, arr2):
    sum1, sum2 = 0, 0
    for i in arr1:
        sum1 += i
    for i in arr2:
        sum2 += i

    return sum1 - sum2


print(find_Missing_Element(arr1, arr2))
print(find_Missing_Element2(arr1, arr2))
