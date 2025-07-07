# upper bound using binary search
# nums[index]> target.... value shoud be greater than the target value but also the smallest

def upper_bound(nums,n,target):
    low = 0 
    high = n-1
    ans = n
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
nums = [1,2,5,6,9,10,12,14,15,18,20,25,26,28,30]
n= len(nums)
target = int(input("Enter any number: "))
print(upper_bound(nums,n,target))