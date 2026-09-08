# Kth Missing Positive Number
# using linear search
arr = [2,3,4,7,11] 
k = 5
for i in range(len(arr)):
    if arr[i]<=k:
        k += 1
    else: break
print(k)