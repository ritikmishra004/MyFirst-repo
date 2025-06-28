# finding missing number
arr = [3,2,5,1]
n = len(arr)+1

total = n*(n+1)//2
summ = 0
for i in range(len(arr)):
    summ += arr[i]
# by not using for we can do this
actual_sum = sum(arr)
print(total-actual_sum)


print("missing number :",total-summ)