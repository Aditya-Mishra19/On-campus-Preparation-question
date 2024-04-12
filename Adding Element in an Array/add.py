def insertBegin(value, arr, N):
    nums = [0] * (N+1) 
    for i in range(len(arr) -1, -1, -1):
        nums[i+1] = arr[i]
    nums[0] = value
    print(*nums)

def insertEnd(value, arr, N):
    arr.append(value)
    print(*arr)

def insertMiddle(value, arr, N, location):
    nums = [0] * (N+1)
    for i in range(location):
        nums[i] = arr[i]

    for i in range(location, N):
        nums[i+1] = arr[i] 
    nums[location] = value
    print(*nums)


arr = [1,2,3,4,5,6]
insertBegin(100, arr, len(arr))
insertEnd(200, arr, len(arr))
insertMiddle(90, arr, len(arr), 3)

