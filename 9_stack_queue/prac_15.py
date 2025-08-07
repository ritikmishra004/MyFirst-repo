# 503. Next Greater Element II

def nextGreaterElements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # 🔹 Stack to keep indexes (not values)

    # 🔁 Traverse the array twice (simulate circular array)
    for i in range(2 * n - 1, -1, -1):
        curr_index = i % n  # 🔄 Wrap around circularly

        # 🔁 Pop all elements from stack <= current
        while stack and nums[stack[-1]] <= nums[curr_index]:
            stack.pop()

        # 🔹 Assign result only in first pass
        if i < n:
            if stack:
                result[curr_index] = nums[stack[-1]]
            # else result[curr_index] remains -1

        # 🔹 Push current index into stack
        stack.append(curr_index)

    return result
