def merge_sort(A):
    if len(A) <= 1:
        return A
    midpoint = int(len(A)/2)
    left, right = merge_sort(A[:midpoint]), merge_sort(A[midpoint:])
    print(left, right)
    return merge(left, right)

def merge(left, right):
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
        
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

def main():
    arr = [5,4,3,2,1]
    sorted = merge_sort(arr)
    print(sorted)

if __name__ == "__main__":
    main()