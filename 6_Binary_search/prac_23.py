# Minimum Number of Days to Make m Bouquets
# optimal approach

def possible(bloomday,mid,m,k):
    count = 0
    no_of_bouquet = 0
    for i in range(0,len(bloomday)):
        if bloomday[i]<=mid:
            count += 1
            if count == k:
                no_of_bouquet += 1
                count = 0
        else:
            count = 0
    return no_of_bouquet >= m
def bouquets(bloomday,m,k):
    if m * k > len(bloomday):
        return -1
    low = min(bloomday)
    high = max(bloomday)
    ans = -1
    while low <= high:
        mid = (low+high)//2
        if possible(bloomday,mid,m,k):
            ans = mid
            high = mid-1
        else:
            low=mid+1
    return ans
bloomday = [7,7,7,7,12,7,7]
m = 2 # number of bouquets
k = 3 # number of different flower in one bouquet
print(bouquets(bloomday,m,k))