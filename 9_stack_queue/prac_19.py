#  trapping water

def trap_rain_water(height):
    n = len(height)
    total_water = 0
    
    for i in range(n):
        # left max for index i
        left_max = max(height[:i+1])
        
        # right max for index i
        right_max = max(height[i:])
        
        # water stored at this index
        water_at_i = min(left_max, right_max) - height[i]
        
        if water_at_i > 0:
            total_water += water_at_i
    
    return total_water

# Example
arr = [4, 2, 0, 3, 2, 5]
print(trap_rain_water(arr))  # Output: 9
