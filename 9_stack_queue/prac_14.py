# 503. Next Greater Element II

def nextGreaterElements(nums):
    n = len(nums)
    result = [-1] * n

    # 🔁 For each element, check next n-1 elements circularly
    for i in range(n):
        for j in range(1, n):
            next_index = (i + j) % n  # 🔄 Circular index
            if nums[next_index] > nums[i]:
                result[i] = nums[next_index]
                break  # 🔚 Found the next greater, break inner loop
    return result

