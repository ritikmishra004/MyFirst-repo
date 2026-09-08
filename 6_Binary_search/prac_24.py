# Find the Smallest Divisor Given a Threshold

import math
def possible(nums,threshold,mid):
    summ = 0
    for i in range(len(nums)):
        summ += math.ceil(nums[i]/mid)
    if summ<=threshold:
        return True
    else:
        return False
def smallestdiv(nums,threshold):
    low = 1
    high = max(nums)
    ans = float('inf')
    while low<=high:
        mid = (low+high)//2
        if possible(nums,threshold,mid)== True:
            ans = mid
            high=mid-1
        else:
            low = mid+1
    return ans
nums = [1,2,5,9]
threshold = 6
print(smallestdiv(nums,threshold))