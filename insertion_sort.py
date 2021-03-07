import time

arr = [7,8,5,4,9,2]

start1 = time.time()
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

print(arr)

# alternate method
arr2 = [7,8,5,4,9,2]

start2 = time.time()
for i in range(1, len(arr2)):
    curNum = arr2[i]
    for j in range(i, 0, -1):
        if arr2[j-1] > curNum:
            arr2[j] = arr2[j-1]
            arr2[j-1] = curNum
        else:
            arr2[j] = curNum
            break

print(arr2)

# output:
# [2, 4, 5, 7, 8, 9]