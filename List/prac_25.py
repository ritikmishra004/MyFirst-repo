# Finding the number that appear once and others are twice

arr = [1,2,3,4,5,6,6]
n = len(arr)

for i in range(0,n):
    num = arr[i]
    count =0
    for j in range(n):
        if num == arr[j]:
            count+=1
    
    if count == 1:
        print("one :",num)