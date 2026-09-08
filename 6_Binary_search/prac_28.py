# aggressive cows
# now we are learning new pattern of binary search
# pattern is min (max) and max(min)
# in this question we have to put the cows in the type of distance in which the minimum distance between cows is the max
# of any other type of setteling them in the array...

# BRUTE FORCE APPROACH
def canweplace(arr,dis,cows):
    count_cow = 1
    last = arr[0]
    for i in range(1,len(arr)):
        if arr[i]-last >= dis:
            count_cow += 1
            last = arr[i]
    if count_cow >=cows:
        return True
    else:
        return False
def aressive(arr,cows,n):
    low = min(arr)
    high = max(arr)
    for i in range(0,(high-low)+1):
        if canweplace(arr,i,cows)== True:
            continue
        else:
            return i-1

arr = [0, 3, 4, 7, 10, 9]
cows = 4
n = len(arr)
print(aressive(arr,cows,n))