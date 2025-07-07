# find the first and last occurence of x
# using binary search
# with the help of lower bound and upper bound
# time O(log n)

def find_first(nums, n, target):
    low = 0
    high = n - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            first = mid
            high = mid - 1  # search left for first occurrence
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first

def find_last(nums, n, target):
    low = 0
    high = n - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            last = mid
            low = mid + 1  # search right for last occurrence
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last

def occurrence(nums, n, target):
    first = find_first(nums, n, target)
    last = find_last(nums, n, target)
    return first, last

nums = [2, 4, 6, 8, 8, 8, 9, 10, 11, 12]
n = len(nums)
x = int(input("Enter any number: "))
print(occurrence(nums, n, x))
