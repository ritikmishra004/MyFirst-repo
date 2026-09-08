# search in rotated sorted array
# revise again
# check the sorted part

def search(nums,n,target):
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return nums[mid]
        

        #left sorted
        if nums[low] <= nums[mid]:
            # 🟢 Left sorted hai

            # 🔹 Check karo target left sorted part mein aata hai ya nahi
            if nums[low] <= target and target <= nums[mid]:
                # 🔹 Target left part mein hai, to right hatao
                high = mid - 1
            else:
                # 🔹 Target left mein nahi hai, to left hatao
                low = mid + 1

        # right sorted
        else:
            if nums[mid]<=target and target<=nums[high]:
                low = mid+1
            else:
                high=mid-1
    return -1

nums = [7,8,9,1,2,3,4,5,6]
n=len(nums)
target = int(input("enter any number: "))
print(search(nums,n,target))