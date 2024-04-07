from collections import defaultdict

def getFreq(arr):
    store = defaultdict(int)
    for num in arr:
        store[num] += 1
    
    for key, val in store.items():
        print(key, val)


getFreq([10,5,15,10,5])