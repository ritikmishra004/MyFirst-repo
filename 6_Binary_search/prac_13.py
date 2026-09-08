# Find out how many times has an array been rotated


def findKRotation(arr):
    low = 0
    high = len(arr) - 1
    ans = float('inf')   # Ab tak ka minimum number
    index = -1           # Uska index = rotation count

    while low <= high:
        mid = (low + high) // 2

        # 🔹 Agar current part sorted hai
        if arr[low] <= arr[high]:
            if arr[low] < ans:
                ans = arr[low]
                index = low
            break

        # 🔹 Left half sorted hai
        if arr[low] <= arr[mid]:
            if arr[low] < ans:
                ans = arr[low]
                index = low
            low = mid + 1

        # 🔹 Right half sorted hai
        else:
            if arr[mid] < ans:
                ans = arr[mid]
                index = mid
            high = mid - 1

    return index

arr = [4, 5, 6, 7, 0, 1, 2, 3]
print("Rotated:", findKRotation(arr))  