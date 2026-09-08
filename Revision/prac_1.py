nums = [1,2,3,4,5,6,7]
n = len(nums)
k = 3
k = k%n
temp = []
for i in range(k):
    temp.append(nums[n-k+i])
print(temp)

for i in range(k,-1,-1):
    nums[i+k] = nums[i]
print(nums)

for i in range(0,k):
    nums[i]=temp[i]

print(nums)