# moving all the non zeroes in the end of the array

arr = [1,0,2,3,4,5,0,7,6,0,8,0]
n = len(arr)

temp = []
for i in range(0,n):
    if arr[i]>0:
        temp.append(arr[i])

for i in range(0,len(temp)):
    arr[i] = temp[i]

for i in range(len(temp),n):
    arr[i] = 0

print(arr)