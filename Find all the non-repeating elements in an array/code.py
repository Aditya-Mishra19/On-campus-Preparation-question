from collections import defaultdict
def solve(arr, N):
    store = defaultdict(int)
    for num in arr:
        store[num] += 1
    for k, v in store.items():
        if v == 1:
            print(k, end = " ")

solve([1,1,2,2,3], 6)