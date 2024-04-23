from collections import *

def solve(arr):
    store = defaultdict(int)
    for num in arr:
        store[num] += 1 
    ans = sorted(store.items(), key = lambda item : item[1], reverse = True)
    print("Sorted by frequency: \n",ans)
    for num in ans:
        first, second = num
        for i in range(second):
            print(first, end = " ")


arr = [1,1,1,2,2,2,2,2,3,3,3,3,3,3,4,5,5,0]
N = len(arr)
solve(arr)