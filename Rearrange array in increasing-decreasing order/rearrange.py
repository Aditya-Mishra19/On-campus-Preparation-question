def solve():
    arr = [8,7,1,2,3,9]
    arr.sort() 
    n = len(arr)
    for i in range(n // 2):
        print(arr[i], end = " ")
    
    for i in range(n - 1, n // 2 - 1, -1):
        print(arr[i], end = " ")

solve()