# second largest 

arr = list(map(int,input("Enter numbers : ").split()))
n = len(arr)

largest = arr[0]
slargest = float('-inf')  # ✅ safest small value
# works for all values including negative

for i in range(n):
    if arr[i] > largest:
        slargest = largest
        largest = arr[i]
    elif arr[i] < largest and arr[i] > slargest:
        slargest = arr[i]

print("second largest : ", slargest)