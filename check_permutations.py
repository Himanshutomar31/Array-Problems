#check whether two string are permutations of each other

#O(nlogn)
def check_permutations(s1, s2):
    res1 = ''.join(sorted(s1))
    res2 = ''.join(sorted(s2))
    if res1 == res2:
        return True
    else:
        return False

#O(n)
def check_permutations2(s1, s2):
    d = dict()
    for i in s1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in s2:
        if i in d:
            d[i] -= 1
        else:
            return False
    for i in d:
        if d[i] != 0:
            return False
    return True

s1 = "AACC"
s2 = "CACA"
print(check_permutations(s1, s2))
print(check_permutations2(s1, s2))
