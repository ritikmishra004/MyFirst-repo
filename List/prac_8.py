# Rotate an array by one

arr = [1,2,3,4,5,6,7,8]
n = len(arr)

temp = arr[0]

for i in range(1,n):
    arr[i-1] = arr[i]

arr[n-1] = temp

print(arr)