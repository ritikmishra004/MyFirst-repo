# second largest number 

arr = list(map(int, input("Enter number : ").split()))
n = len(arr)

largest = arr[0]
for i in range(n):
    
    if arr[i] > largest:
        largest = arr[i]

print("largest element : ",largest)
second_largest = 0
for i in range(n):
    #second_largest = 0..agr ye upr na likh kr loop mei likhoge to har bar largest aur 2nd large update hoga
    if arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print("second largest element : ",second_largest)