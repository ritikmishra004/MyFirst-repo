# Longest consecutive sequence
# optimal approach

arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]

# ✅ Step 1: convert to set to remove duplicates and allow O(1) lookup
s = set(arr)

# ❌ Tum indexing use kar rahe the (s[0]), lekin set mein indexing nahi hoti
# ✅ Isiliye set ko list bana ke sort karte hain
s = sorted(s)

# ✅ Initialization
current_count = 1
longest = 1
last_smallest = s[0]

# ✅ Loop through sorted list
for i in range(1, len(s)):
    if s[i] - 1 == last_smallest:         # 🔸 consecutive hai
        current_count += 1
        last_smallest = s[i]
    else:                                 # 🔸 sequence break ho gaya
        current_count = 1
        last_smallest = s[i]                  # 🔸 update last element
    longest = max(longest, current_count) # 🔸 update max length

print(longest)
