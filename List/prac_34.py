# sort an array 0's,1's,and 2's

arr = [1,2,0,1,0,2,1,0,0,2,1,1,0,2,1]
n = len(arr)
c1,c2,c3 = 0,0,0
for i in range(n):
    if arr[i]== 0:
        c1 += 1
    elif arr[i]== 1:
        c2 += 1
    else:
        c3 += 1

for i in range(0,c1):
    arr[i]=0
for i in range(c1,c1+c2):
    arr[i]=1
for i in range(c1+c2,n):
    arr[i]=2

print(arr)