def solve(arr,N):
    unique = []
    for i in range(N):
        if arr[i] not in unique:
            unique.append(arr[i])
    print(unique)

arr = [4,4,1,1,2,2,3,3]
N = len(arr)
solve(arr, N)