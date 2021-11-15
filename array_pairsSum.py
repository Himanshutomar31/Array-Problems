def print_pairs(arr, l, sum):
    s = set()
    for i in arr:
        res = sum - i
        if res in s:
            print("Pairs Found", i, res)
        else:
            s.add(i)

A = [11, 15, 6, 8, 9, 10,7]
n = 16
print_pairs(A, len(A), n)
