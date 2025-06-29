# longest subarray with sum k

arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
K = 10
length = 0

for i in range(n):
    for j in range(i,n):
        sum =0
        for k in range(i,j+1):
            sum += arr[k]
        if sum == K:
            length = max(length,j-i+1)

print (length)