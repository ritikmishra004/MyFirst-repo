# longest subarray with sum k
# using two loops

arr = [1,2,3,1,1,1,1,4,5,6,7,8,9,10,11,12,13]
n = len(arr)
K = 5
length = 0

for i in range(n):
    sum =0
    for j in range(i,n):
        sum += arr[j]

        if sum == K:
            length = max(length,j-i+1)

print(length)