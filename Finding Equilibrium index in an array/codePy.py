def solve(arr, N):
    pre, suf = [0] * N, [0] * N 
    pre[0], suf[N-1] = arr[0], arr[N-1]
    for i in range(1, N):
        pre[i] = pre[i-1] + arr[i]
    for i in range(N-2, -1, -1):
        suf[i] = suf[i + 1] + arr[i]
    print(pre,'\n', suf)
    for i in range(N):
        if pre[i] == suf[i]:
            return i 
    return -1

def solve2(arr, N):
    total = sum(arr)
    left, right = 0, total 
    for i in range(N):
        right -= arr[i]
        if left == right:
            return i 
        left += arr[i]
    return -1

nums = [2,3,-1,8,4]
n = len(nums)
print("2. Equilibrium point: ", solve2(nums, n))