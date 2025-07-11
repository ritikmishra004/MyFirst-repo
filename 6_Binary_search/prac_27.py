# Kth Missing Positive Number
# using binary search
# humare pass array hai to une last index wale no. ko check karenge aur index+1 jo ke actual number hai usse subtract
# karenge to usse pta chal jayega ke kitne no missing hain 
# ishi observation ke help se hum binary search ka use kr skte hain

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
