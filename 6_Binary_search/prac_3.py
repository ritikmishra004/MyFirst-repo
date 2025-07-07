# lower bound
# target =< nums[index] means find soimething which is greater or equal to the target

def lower_bound(nums,n,target):
    low = 0
    high = n-1
    ans=n
    while low<=high:
        mid = (low+high)//2
        if nums[mid] >= target:
            ans = mid
            high =mid-1
        else:
            low=mid+1
    return ans


nums = [1,2,5,6,9,10,12,14,15,18,20,25,26,28,30]
n= len(nums)
target = int(input("Enter any number: "))
print(lower_bound(nums,n,target))