def multiply(mid, n):
    # mid^n calculate karne ke liye helper function
    ans = 1
    for _ in range(n):
        ans *= mid
    return ans

def nth_root(n, m):
    low = 1
    high = m
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        val = multiply(mid, n)  # mid^n calculate karo
        
        if val == m:
            return mid  # ✅ perfect nth root mil gaya
        elif val < m:
            ans = mid         # store current best
            low = mid + 1     # right part me jaao (bada number try karo)
        else:
            high = mid - 1    # left part me jaao (chhota number try karo)

    return ans  # Agar exact match na mile to approx (floor value) dega

# User Input
n = int(input("Enter the nth root you want to find (n): "))
m = int(input("Enter the number (m): "))

print(f"The {n}th root of {m} is:", nth_root(n, m))
