# rotate an arry by k places

arr = list(map(int,input("Enter numbers : ").split()))
n = len(arr)
d = int(input("Enter any number: "))
# if the d is greater than the n
d = d%n

temp = []
# taking d numbers in temprary array
for i in range(0,d):
    temp.append(arr[i])

# shifting the numbers
for i in range(d,n):
    arr[i-d] = arr[i]

# taking numbers from temprary and save it in original arr
j = 0
for i in range(n-d,n):
    arr[i] = temp[j]
    j +=1

print("rotated array : ",arr)