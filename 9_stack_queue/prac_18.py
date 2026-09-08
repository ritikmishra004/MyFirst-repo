#  trapping water

def trap_rain_water(height):
    n = len(height)
    if n == 0:
        return 0
    
    # Step 1: Prefix max (left_max array)
    left_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    
    # Step 2: Suffix max (right_max array)
    right_max = [0] * n
    right_max[-1] = height[-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    
    # Step 3: Calculate water
    total_water = 0
    for i in range(n):
        water_at_i = min(left_max[i], right_max[i]) - height[i]
        if water_at_i > 0:
            total_water += water_at_i
    
    return total_water

# Example
arr = [4, 2, 0, 3, 2, 5]
print(trap_rain_water(arr))  # Output: 9
