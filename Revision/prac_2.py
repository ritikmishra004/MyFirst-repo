nums = [1, 2, 1, 3, 4, 2, 3]
k = 4
n = len(nums)
window = []
count = []
for i in range(k):
  window.append(nums[i])
distinct = len(set(window))
count.append(distinct)
for i in range(k,n):
  window.pop(0)
  window.append(nums[i])
  distinct = len(set(window))
  count.append(distinct)
print(count)
