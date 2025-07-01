# # sort an array 0's,1's,and 2's using (dutch national flag algorith)
# Dutch National Flag Algorithm:
# This algorithm is used to sort an array containing only 0s, 1s, and 2s in a single traversal (O(n) time and O(1) space).
#  0 to low-1      → all 0s
#  low to mid-1    → all 1s
#  mid to high     → unknown (unsorted)
#  high+1 to n-1   → all 2s

arr = [1,2,0,1,0,2,1,0,0,2,1,1,0,2,1]
n = len(arr)

low = 0
mid = 0
high = n-1
while mid<=high:
    if arr[mid] == 0:   # actually it is checking from the mid to high-1 wala part
        # yhn pr assume karo 0-(low-1)=0,low-(mid-1)=1,mid-(high-1)= unsorted,high-(n-1)=2
        arr[low],arr[mid]=arr[mid],arr[low]
        low += 1
        mid += 1
    elif arr[mid]== 1:
        mid +=1
    else:
        arr[mid],arr[high]=arr[high],arr[mid]
        high -= 1

print(arr)