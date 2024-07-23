
arr = list(map(int,input().split()))
for i in range(len(arr)):
    for j in range (i,len(arr)):
        if arr[j] < arr [i]:
            arr[j] , arr[i] = arr[i] , arr[j]

print(*arr)

