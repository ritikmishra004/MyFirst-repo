from collections import defaultdict

# Input
n = int(input())
arr = list(map(int, input().split()))

# Precompute frequency
mp = defaultdict(int)
for num in arr:
    mp[num] += 1

# Iterate over the map
for key in sorted(mp.keys()):
    print(f"{key}->{mp[key]}")

# Queries
q = int(input())
for _ in range(q):
    number = int(input())
    print(mp[number])
