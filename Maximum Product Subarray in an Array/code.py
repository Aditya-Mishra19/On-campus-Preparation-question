def solve(arr, n):
    maxP = 0
    sufx, prex = 1, 1
    for i in range(n):
        if arr[i] == arr[n-i-1] and arr[i] == 0:
            sufx, prex = 1, 1
        else:
            prex *= arr[i]
            sufx *= arr[n-i-1]
        maxP = max(maxP, max(prex, sufx))
    print("Maximum Product: ", maxP)

arr = [1,2,-3,0,-4,-5]
N = len(arr)
solve(arr, N)