arr = [1, 20, 2, 10]
# arrSum =  33
# R0 = 54
# R1 = 25
# R1 - R0 = 29
# R2 = 72
# R2 - R1 = 47
# R3 = 47
# R3 - R2 = 25
#Rj - Rj-1 = arrSum - n * arr[n-j]
#           = 54 + 33 - 4 * 10

# O(n^2)
def find_max_sum(arr):
    max = -1
    l = len(arr)
    for i in range(l):
        sum = 0
        j=i
        for k in arr:
            sum = sum + j*k
            j+=1
            if (j == l):
                j = 0

        if (max < sum):
            max = sum

    return max


def maxSum(arr):
    arrSum = 0
    currVal = 0

    n = len(arr)

    for i in range(0, n):
        arrSum = arrSum + arr[i]
        currVal = currVal + (i * arr[i])

    maxVal = currVal

    for j in range(1, n):
        currVal = currVal + arrSum - n * arr[n - j] # 10 * arr[9]
        if currVal > maxVal:
            maxVal = currVal

    return maxVal


print(maxSum(arr))