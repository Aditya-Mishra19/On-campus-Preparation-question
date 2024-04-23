from collections import defaultdict
def solve(arr, N):
    store = {}
    print("Symmetric Pairs are: ")
    for nums in arr:
        first, second = nums 
        if second not in store:
            store[first] = second 
        else:
            print((first, second), end = " ")


arr = [[1, 2], [2, 1], [3, 4], [4, 5], [5, 4]]
N = len(arr)
solve(arr, N)