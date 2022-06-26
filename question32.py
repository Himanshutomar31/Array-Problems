def get_string(n):
    if n == "1":
        return "abcd"
    if n == "2":
        return "ef"
    if n == "3":
        return "g"
    if n == "4":
        return "hz"
    if n == "5":
        return "i"
    return ""


def permute(num):
    lst = list()  # ['g','ef','hzdef']
    for i in num:
        lst.append(get_string(i))

    print(lst)
    n = len(lst)
    res = list()
    ind = -1
    s = ""
    res.append(lst[0])
    for i in range(1, n):
        j = 0
        temp = res[:]
        res.clear()
        while j < len(lst[i]):
            for k in temp:
                t = k+lst[i][j]
                res.append(t)
            j += 1

    print(res)


n = "324"
permute(n)
