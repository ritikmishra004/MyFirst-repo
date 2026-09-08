def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])     # Recursively sort left
    right = merge_sort(arr[mid:])    # Recursively sort right

    return merge(left, right)        # Merge sorted parts

def merge(left, right):
    result = []
    i = j = 0

    # Merge step
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Driver
arr = list(map(int, input("Enter elements: ").split()))
arr[:] = merge_sort(arr)  # ✅ Copy back sorted data into original arr
print("Sorted array:", arr)
