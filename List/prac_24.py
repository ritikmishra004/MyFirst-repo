# Maximum consicutive ones

arr = [1,1,0,1,1,1,0,1,1]
n = len(arr)
maxi = 0
count = 0

for i in range(0,n):
    if arr[i] == 1:
        count +=1
        maxi = max(maxi,count)
    else:
        count = 0

print(maxi)