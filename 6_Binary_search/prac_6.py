# upper bound using bisect module

import bisect

nums = [2,5,8,10,15,22,63,87]
target = int(input("Enter any number: "))
index = bisect.bisect_right(nums,target)
print(index)