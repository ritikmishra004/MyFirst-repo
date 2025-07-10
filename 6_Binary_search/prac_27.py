# Kth Missing Positive Number
# using binary search

def findKthPositive(arr, k):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Number of missing elements till index mid:
        missing = arr[mid] - (mid + 1)

        if missing < k:
            low = mid + 1
        else:
            high = mid - 1

    return low + k

# Example:
arr = [2, 3, 4, 7, 11]
k = 5
print(findKthPositive(arr, k))  # Output: 9
