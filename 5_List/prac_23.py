# Zeros on lefd and right

arr = [1,0,2,0,4,5,0,6]
n= len(arr)

j = 0
for i in range(0,n):
    if arr[i] != 0:
        arr[i],arr[j]=arr[j],arr[i]
        j+=1
print(arr)

j=0
for i in range(0,n):
    if arr[i] == 0:
        arr[i],arr[j]=arr[j],arr[i]
        j+=1

print(arr)