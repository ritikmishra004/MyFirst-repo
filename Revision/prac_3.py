nums = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
n = len(nums)
threshold = 4
window = 0
count = 0
for i in range(k):
  window +=nums[i]
if (window/k)>=threshold:
  count +=1
for i in range(k,n):
  window = window-nums[i-k]+nums[i]
  if (window/k)>=threshold:
    count+=1
print(count)