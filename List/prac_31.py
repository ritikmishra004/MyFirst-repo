# Two sum

arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
k = int(input("enter numbers: "))
found = False

for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j] == k:
            print("yes",i,j)
            found = True
            break
    if found:
        break
if not found:
    print("invalid: no match")