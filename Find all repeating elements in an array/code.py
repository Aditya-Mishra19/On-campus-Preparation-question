from collections import defaultdict
def solve(arr, N):
    store = defaultdict(int)
    for num in arr:
        store[num] += 1
    print(store)
    for k, v in store.items():
        print(k, end = " ")

solve([1,1,2,2,3,3], 6)