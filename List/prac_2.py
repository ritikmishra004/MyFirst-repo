# finding largest element using pointer

arr = list(map(int,input("Enter any number: ").split()))
n = len(arr)

largest = arr[0]
for i in range(n):
    
    if arr[i] > largest:
        largest = arr[i]

print("largest element : ",largest)