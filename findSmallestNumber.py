def getMin(arr):
    minElement = float('inf')
    for i in range(len(arr)):
        minElement = min(minElement, arr[i])
    return minElement

arr = [2,1,4,5]
res = getMin(arr)
print("Minimum element: ", res)