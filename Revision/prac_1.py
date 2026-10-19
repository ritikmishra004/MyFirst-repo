nums = [1, 5, 1, 5]
target = 6
n = len(nums)
ans = []
hash = {}
for i in range(n):
  diff =target-nums[i]
  if diff in hash:
    ans.append((diff,nums[i]))
    del hash[diff]
  else:
    hash[nums[i]] = i

print (ans)