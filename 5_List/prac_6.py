# check if the array is sorted 

arr =list(map(int,input("Enter numbers : ").split()))
n = len(arr)
is_sorted = True

for i in range(1,n):
    if arr[i] >= arr[i-1]:
        is_sorted = True
    else:
        is_sorted = False
        break

print("array is sorted", is_sorted)