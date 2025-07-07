# search in rotated sorted array
# revise again
# Trim down the condition of duplicates which can be the problem

def search(nums,n,target):
    low = 0 
    high =n-1
    while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return True
            if nums[low]==nums[mid] and nums[mid]==nums[high]:
                low += 1
                high-=1
                continue
            if nums[low]<=nums[mid]:
                if nums[low]<=target and target<=nums[mid]:
                    high = mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<= target and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
    return False
nums = [3,1,2,3,3,3,3]
n = len(nums)
target = int(input("Enter any number: "))
print(search(nums,n,target))