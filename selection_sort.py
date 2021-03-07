arr = [7,8,5,4,9,2]

for i in range(len(arr)):
    minIndex = i
    for j in range(i, len(arr)):
        if arr[j] < arr[minIndex]:
            minIndex = j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]

print(arr)
    
# output :
# [2, 4, 5, 7, 8, 9]