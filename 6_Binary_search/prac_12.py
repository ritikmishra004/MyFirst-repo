# find the minimum in sorted rotated array

def mini(nums,n):
    import sys
    low = 0
    high = n-1
    ans = +sys.maxsize
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>=nums[low]:
            ans = min(ans,nums[low])
            low = mid+1
        else:
            ans = min(ans,nums[mid])
            high = mid-1
    return ans
nums = [4,5,6,7,0,1,2,3]
n = len(nums)
print(mini(nums,n))