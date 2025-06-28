# intersection of two sorted array

arr = [2,3,3,4,4,5,6,7,8]
arr1 = [1,2,3,3,4,5,6,7,8,9]

intersection = []
i = 0
j = 0

while i < len(arr) and j < len(arr1):
    if arr[i]<arr1[j]:
        i += 1
    elif arr1[j]<arr[i]:
        j += 1
    else:
        intersection.append(arr[i])
        i += 1
        j += 1

print(intersection)