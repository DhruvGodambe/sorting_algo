arr = [7,8,5,4,9,2]

for i in range(len(arr)-1):
    for j in range(len(arr) -1 - i):
        if arr[j+1] < arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)

# output:
# [2, 4, 5, 7, 8, 9]