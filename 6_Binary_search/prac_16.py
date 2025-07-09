# find peak element
# nums[i-1] < nums[i] > nums[i+1]
# optimal
# if mid is greater the peak is on the right.    1 2 3 4 [5] 6 7 8 0
# if mid is smaller the peak is on the left      1 2 3 7 [5] 6 7 8 
def peak(nums,n):
    if n == 1:
        return nums[0]
    if nums[0]>nums[1]:
        return nums[0]
    if nums[n-1]>nums[n-2]:
        return nums[n-1]
    
    high = n-2
    low = 1
    while low<=high:
        mid = (low+high) //2
        if (nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
            return nums[mid]
        if nums[mid]>nums[mid-1]:
            low = mid+1
        else:
            high = mid-1
    
nums = [1,2,3,4,5,6,7,8,5,0]
n = len(nums)
ans = peak(nums, n)
print("Index of Peak:", ans)
