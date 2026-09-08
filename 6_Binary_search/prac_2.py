# Binary search
# recursive code

def binary_search(nums,low,high,target):
    if low>high:
        return -1
    mid = (high+low)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        return binary_search(nums,mid+1,high,target)
    
    return binary_search(nums,low,mid-1,target)
    
nums = [2,3,4,5,6,7,8,9,10,11,12,13]
n= len(nums)
target = int(input("enter any number : "))
print(binary_search(nums,0,n-1,target))