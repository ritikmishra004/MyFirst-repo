# sum of sub arrays minimum
# brute force

# Sum of Subarrays Minimum (Brute Force) with MOD

def mini_sum(arr):
    MOD = 10**9 + 7  # 🔹 Large prime number to prevent overflow
    total = 0        # 🔹 Final sum of all subarray minimums
    for i in range(len(arr)):
        mini = arr[i]   # Current subarray ka minimum
        for j in range(i, len(arr)):
            mini = min(arr[j], mini)   # Update minimum element
            total = (total + mini) % MOD  # Mod lagake sum update
    return total

arr = [3, 1, 2, 4]
print(mini_sum(arr))  # Output: 17

'''Competitive programming me answers bahut bade numbers ban sakte hain.

Python me int unlimited hota hai, lekin constraints me required hota hai ki answer ko kisi fixed range (usually 
10^9+7) me rakha jaye.
Ye overflow prevent karta hai (C++/Java me zaroori) aur problem ke output format ke saath match karta hai.'''