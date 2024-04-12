def getAvg(arr, N):
    sumOfArr = 0 
    for num in arr:
        sumOfArr += num 
    avg = sumOfArr / N 
    print(avg)



arr = [1,2,3,4,5,6]
N = len(arr)
getAvg(arr, N)