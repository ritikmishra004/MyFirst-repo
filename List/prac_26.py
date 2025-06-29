# Finding the number that appear once and others are twice

arr = [1,1,2,2,3,3,4,5,5,6,6]
n = len(arr)

hashmap = {}

for num in arr:
    # hashmap.get(num, 0) returns current count (or 0 if not present)
    #  +1 to increment count
    hashmap[num] = hashmap.get(num,0)+1 # ye saare element ko store karayega hashmap mei .get ke through
# +1 kar dega agr dubara ayega number

# 🔸 Find the element that occurs only once
for num, count in hashmap.items():  # ✅ .items() gives (key, value) pairs
    # ✅ num = element, count = frequency
    if count == 1:
        print(num) # return the single non-repeating number