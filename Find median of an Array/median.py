def getMedian(N, arr):
    arr.sort()
    if N % 2 == 0:
        ind1 = (N // 2) - 1
        ind2 = (N // 2)
        return (arr[ind1] + arr[ind2]) / 2
    return arr[N//2]


arr = [4,7,1,2,5,6]
N = len(arr)
print(getMedian(N, arr))