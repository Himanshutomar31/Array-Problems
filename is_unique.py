# O(n^2)
def is_unique(s1):
    check = True
    for i in range(0, len(s1)):
        for j in range(i+1, len(s1)):
            if s1[i] == s1[j]:
                check = False
                break
    if check:
        print("Array has all unique characters.")
    else:
        print("Array doesn't has all unique characters.")

#O(N)
def is_unique_char(s1):
    count_lst = [False for i in range(256)]
    for i in s1:
        res = int(ord(i))
        if count_lst[res]:
            return False
        else:
            count_lst[res] = True
    return True

s1 = 'himansu'
is_unique(s1)
print(is_unique_char(s1))


