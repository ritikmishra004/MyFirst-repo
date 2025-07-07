# two sum: using two pointer
# if the array is sorted

arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
k = int(input("enter number: "))
i = 0
j = n-1

while i<j:
    carry_sum = arr[i]+arr[j]
    if carry_sum == k:
        print(i,j)
        break
    elif carry_sum<k:
        i+=1
    else:
        j+=1
else:
    print("not found")