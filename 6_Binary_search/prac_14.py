# Single Element in a Sorted Array
# O(log n)
# think about even and odd index.. because you can se (1,1) are in even and odd index
# but (6,6) are in odd and even index

def single(nums,n):

    if n==1:
        return nums[0]
    if nums[0]!=nums[1]:      # ye hum isliye karte hain kyunki inke left aur right mei chek krne ke
        return nums[0]        # liye koi element nahi hota hai to hum ise pehle he deal kr skte hain
    if nums[n-1]!=nums[n-2]:
        return nums[n-1]
    
    low = 1
    high = n-2

    while low <= high:
        mid = (low+high)//2

        # ✅ Step : Check karo kya mid element akela hai (unique)
        if nums[mid-1]!=nums[mid] and nums[mid]!=nums[mid+1]:
            return nums[mid]

        #  Step: Binary search elimination logic
        #  Concept: har pair even-odd index pe hota hai
        # Agar mid even hai → pair hona chahiye right mein
        # Agar mid odd hai → pair hona chahiye left mein
        # Agar pair correct jagah par hai to single element aage hoga
        if ((mid%2 == 1 and nums[mid-1]==nums[mid]) or (mid%2==0 and nums[mid]==nums[mid+1])):
            low = mid+1   #  Move right
        else:
            high = mid -1  #  Move left

nums = [1,1,2,2,3,3,4,4,5,6,6,7,7,8,8]
n = len(nums)
print(single(nums,n))