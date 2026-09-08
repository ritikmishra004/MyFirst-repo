# Binary search
# itrative code

def binary_search(arr,key):
    n = len(arr)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]== key:
            return mid
        elif arr[mid]<key:
            low = mid+1
        else:
            high = mid-1
    return -1


arr = [3,4,5,6,7,8,9,10,11,12,13,14]
n = len(arr)
key = int(input("Enter any number : "))
print(binary_search(arr,key))
