
nums = [1, 5, 1, 5]
target = 6

seen = set()
pairs = set()

for num in nums:
    diff = target - num

    if diff in seen:
        pair = tuple(sorted((num, diff)))
        pairs.add(pair)

    seen.add(num)

print(list(pairs))
