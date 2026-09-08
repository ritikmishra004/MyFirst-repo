# Nearest smallest integer

def nearestSmall_integer(arr):
    result = [-1] * len(arr)
    stack = []
    
    for i in range(len(arr)):
        current = arr[i]
        # Jab tak stack ka top current se bada ya equal hai, pop karo
        while stack and stack[-1] >= current:
            stack.pop()
        # Agar stack khali nahi hai, to top hi nearest smaller hoga
        if stack:
            result[i] = stack[-1]
        # Current ko stack me push karo
        stack.append(current)
    return result

arr = [2, 10, 1, 11, 9, 23, 6]
print(nearestSmall_integer(arr))
