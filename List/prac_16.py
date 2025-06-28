# union of two sorted array

arr1 = [1,2,3,4,5,6,7]
arr2 = [1,2,3,4,5,6,7,8,9,10]

union = []

n1 = len(arr1)
n2 = len(arr2)
i = 0
j = 0

while i < n1 and j < n2:
    if arr1[i] <= arr2[j]:
        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    else:
        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr1[j])
        j += 1
while i < len(arr1):
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i+=1
while j < len(arr2):
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j+=1

print(union)