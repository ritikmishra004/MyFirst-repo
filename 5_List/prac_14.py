# union of two sorted array

arr = [1,2,3,4,6,7]
arr2 =[1,2,3,4,5,10,7,8,9]

s = set()
union = []

for i in range(0,len(arr)):
    s.add(arr[i])

for i in range(0,len(arr2)):
    s.add(arr2[i])

for val in s:
    union.append(val)
union.sort()

print(union)