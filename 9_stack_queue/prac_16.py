# Nearest smallest integer

def nearestSmallestInteger(arr):
    result = [-1] * len(arr)  # Pehle se -1 fill kar diya
    for i in range(len(arr)):
        for j in range(i-1, -1, -1):  # Left side se check karte hue
            if arr[j] <= arr[i]:
                result[i] = arr[j]
                break
    return result

arr = [2, 10, 1, 11, 13, 9, 0]
print(nearestSmallestInteger(arr))