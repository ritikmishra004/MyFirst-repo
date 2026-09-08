def sum_subarray_mins(arr):
    MOD = 10**9 + 7
    n = len(arr)
    
    # 🔹 Step 1: Previous Smaller Element (strictly smaller)
    prev_smaller = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        prev_smaller[i] = stack[-1] if stack else -1
        stack.append(i)
    
    # 🔹 Step 2: Next Smaller Element (smaller OR equal)
    next_smaller = [n] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            idx = stack.pop()
            next_smaller[idx] = i
        stack.append(i)
    
    # 🔹 Step 3: Contribution calculation
    total = 0
    for i in range(n):
        left_count = i - prev_smaller[i]     # kitne elements left me cover karega
        right_count = next_smaller[i] - i    # kitne elements right me cover karega
        total = (total + arr[i] * left_count * right_count) % MOD
    
    return total

# Example
arr = [3, 1, 2, 4]
print(sum_subarray_mins(arr))  # Output: 17
