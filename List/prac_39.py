# longest subarray using kedane's algorithm
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
import sys
nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)

maxi = -sys.maxsize-1
sum = 0 
for i in range(n):
    
    sum += nums[i]

    if sum > maxi:
        maxi = sum
    
    if sum < 0:
        sum = 0

print (maxi)