# Capacity To Ship Packages Within D Days

# in this case we know the minimum capacity of the ship is more than the arrays maximum weighted number 
# or the second hint is that the capicity is between the maximum weight or sumation of array
# [1,2,3,4,5,6,7,8,9,10] = 55.    capacity = 10-55

# Ye function check karta hai ke 'mid' capacity ke saath kitne din lagenge saari weights ko ship karne mein
def time(nums, mid):
    day = 1         # Pehla din se start
    load = 0        # Current din ka load
    for i in range(len(nums)):
        # Agar current item ko daalne se load mid se zyada ho jaye
        if load + nums[i] > mid:
            day += 1            # naye din me shift kar do
            load = nums[i]      # naye din ka pehla load
        else:
            load += nums[i]     # current din mein load add kar do
    return day                  # total din return karo

def ship(nums,days):
    low = max(nums)
    high = sum(nums)
    # ans = float('inf')
    while low<=high:
        mid = (low+high)//2
        if time(nums,mid)<=days:
            high=mid-1
        else:
            low=mid+1
    return low
nums = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(ship(nums,days))