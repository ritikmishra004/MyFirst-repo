# koko eating banana
# using binary search

import math

def eatall(speed, piles):
    total_time = 0
    for pile in piles:
        total_time += math.ceil(pile / speed)
    return total_time

def koko(piles, h):
    low = 1
    high = max(piles)
    answer = high

    while low <= high:
        mid = (low + high) // 2
        if eatall(mid, piles) <= h:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer

# Input
piles = [3, 6, 7, 11]
h = 8
print("Minimum speed:", koko(piles, h))
