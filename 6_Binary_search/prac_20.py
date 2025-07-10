# koko eating banana
# using brute force

from math import ceil
# Function to calculate total hours required to eat all bananas at speed 'k'
def time(nums, k):
    total_hours = 0
    for i in range(len(nums)):
        # ceil(nums[i] / k): pile ke liye required hours nikalta hai
        # Total hours me add karte jao
        total_hours += ceil(nums[i] / k)
    return total_hours

# Main function to find minimum possible speed 'k' using brute-force
def koko(nums, hours):
    # Try every speed from 1 to max(nums)
    for k in range(1, max(nums)+1):
        required_time = time(nums, k)  # 🔸 is speed pe total hours chahiye
        if required_time <= hours:
            # Agar required hours <= allowed hours, to ye speed answer hai
            return k

nums = [3, 6, 7, 11]
hours = 8
print("Minimum banana eating speed:", koko(nums, hours))