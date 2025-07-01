# two sum problem using hashing

nums = [2, 3, 6, 8, 4, 5, 12, 15]
target = 18
hash_map = {}

for i in range(len(nums)):
    
    #  Calculate the number we need to reach target
    diff = target - nums[i]
    if diff in hash_map:          # If that number already exists in hash_map, we found the pair

        # ✅ Return indices of both numbers that sum up to target
        print("Indices:", [hash_map[diff], i])   # You can return this in a function
        break
    # If not found, store current number and its index in hash_map
    hash_map[nums[i]] = i
    # eg: hash_map[2] = 0, hash_map[3] = 1, etc.