# floor and ceil in sorted array

def floor_ceil(nums,n,target):
    low = 0 
    high = n-1
    floor = -1
    ceil = -1
    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            floor = nums[mid]
            ceil = nums[mid]
            break
        elif nums[mid] < target:
            floor = nums[mid]
            low=mid+1
        else:
            ceil = nums[mid]
            high= mid-1
    return floor,ceil


nums = [10,20,30,40,50]
n= len(nums)
target = int(input("Enter any number: "))
print(floor_ceil(nums,n,target))