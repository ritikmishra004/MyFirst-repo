# Longest consecutive sequence
# optimal approach

arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]

# ✅ Step 1: convert to set to remove duplicates and allow O(1) lookup
num_set = set(arr)
longest = 0

for num in num_set:
    if num-1 not in num_set:
        current = num
        current_count = 1

        while current+1 in num_set:
            current += 1
            current_count += 1
        
        longest = max(longest,current_count)

print(longest)

# num_set = set(nums)
#         longest = 0
#         for i in num_set:
#             if i-1 not in num_set:
#                 length = 1
#                 while i+length in num_set:
#                     length+=1
#                 longest = max(longest, length)
#         return longest