# find missing number

arr = [2,4,1,5]
# 🔹 Find from 1 to max element of array
for i in range(1, max(arr) + 1):     #maximum number tak check karna
    flag = 0
    for j in range(len(arr)):
        if arr[j] == i:
            flag = 1
            break
    if flag == 0:
        print("missing number : ",i)