arr = [6, 7, 9, 5, 3, 10]
k = 10
ans = -1
for i in range(len(arr)):
    if arr[i] == k:
        ans = i
        break
print("The element is present in", ans, "index")
