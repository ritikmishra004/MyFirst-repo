# lower bound
# using bisect module 

import bisect  # 🔹 bisect module ko import kar rahe hain (binary search based insertion ke liye)

nums = [1, 2, 5, 6, 9, 10, 12]  # 🔹 Sorted list honi chahiye bisect functions ke liye

target = int(input("Enter any number : "))  # 🔹 User se target number input

# 🔹 bisect_left(nums, target) ⇒ return karta hai first index jahan target insert ho sakta hai to maintain sorted order
# Ye basically LOWER BOUND ka kaam karta hai (first index jahan nums[index] >= target ho)

print(bisect.bisect_left(nums, target))  # 🔹 Lower Bound index print karega


# # OTHER FUNCTIONS OF BISECT:

# # 1️⃣ bisect.bisect_right(nums, target)
# # 👉 Returns index where element > target pehli baar aata hai
# # 👉 This is like UPPER BOUND

# print("Upper bound index:", bisect.bisect_right(nums, target))


# # 2️⃣ bisect.insort_left(nums, target)
# # 👉 Sorted list mein target insert karta hai LEFTMOST valid position pe
# # Useful when duplicates allowed and insert pehle chahiye
# # Example:


# bisect.insort_left(nums, target)
# print("After insort_left:", nums)


# # 3️⃣ bisect.insort_right(nums, target)
# # 👉 Sorted list mein target insert karta hai RIGHTMOST valid position pe
# # Useful jab tum duplicate ke baad insert karna chahte ho
# # Example:


# nums = [1, 2, 5, 6, 9, 10, 12]  # reset
# bisect.insort_right(nums, target)
# print("After insort_right:", nums)
