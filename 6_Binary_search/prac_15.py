# find peak element
# nums[i-1] < nums[i] > nums[i+1]
# brute force
def peak(nums,n):
    for i in range(n):
        if ((i==0 or nums[i-1]<nums[i]) and (i==n-1 or nums[i+1]<nums[i])):
            return i
    return -1

nums = [5,4,3,2,1]
n = len(nums)
ans = peak(nums, n)
print("Index of Peak:", ans)
print("Peak element:", nums[ans])