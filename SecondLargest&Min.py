def getSecondLargest(arr):
    if len(arr) < 2:
        return -1
    largest, secondLargest = float('-inf'), float('-inf')
    for num in arr:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest:
            secondLargest = num 
    return secondLargest if secondLargest != float('-inf') else -1

def getSecondMin(arr):
    if len(arr) < 2:
        return -1
    minimum, secondMin = float('inf'), float('inf')
    for num in arr:
        if num < minimum:
            secondMin = minimum
            minimum = num
        elif num < secondMin:
            secondMin = num 
    return secondMin if secondMin != float('inf') else -1


arr = [1,2,3,4,5,6,7]
secondLargest = getSecondLargest(arr)
secondMin = getSecondMin(arr)
print("Second Largest: ", secondLargest, "\nSecond Minimum: ", secondMin)
