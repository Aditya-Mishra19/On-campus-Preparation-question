def getSecondLargest(arr):
    largest, secondLargest = float('-inf'), float('-inf')
    for num in arr:
        if num > largest:
            largest = num
        elif num > secondLargest and num < largest:
            secondLargest = num 
    return secondLargest if secondLargest != float('-inf') else -1

def getSecondMin(arr):
    minimum, secondMin = float('inf'), float('inf')
    for num in arr:
        if num < minimum:
            minimum = num
        elif num < secondMin and num > minimum:
            secondMin = num 
    return secondMin if secondMin != float('inf') else -1


arr = [1]
secondLargest = getSecondLargest(arr)
secondMin = getSecondMin(arr)
print("Second Largest: ", secondLargest, "\nSecond Minimum: ", secondMin)