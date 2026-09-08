# union of two sorted array

arr = [2,5,3,5,0,9,8]
arr2 = [1,2,3,4,10,6,7,8,9]

union = set(arr+arr2)

print("union: ",union)
print(type(union))
print(union)

#type casting union from set to list
union = list(union)
print(type(union))
print(union)