def rotateArray(arr, k, N):
    ans = [0] * N 
    for i in range(N):
        ans[i] = arr[(i + k) % N]
    print(*ans)


arr = [1,2,3,4,5,6,7]
N = len(arr)
k = 2
rotateArray(arr, k, N)