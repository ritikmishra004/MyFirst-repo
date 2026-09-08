# majority Element greator than n/2 using hashing
# using moore's voting algorithm

arr = [1,2,2,1,2,3,1,2,1,3,4,2,2,2,2,2,2,2,5,4,5]
n = len(arr)
count = 0
element = None

for i in range(n):
    if count == 0:
        count +=1
        element = arr[i]
    elif arr[i]== element:
        count +=1
    else:
        count -= 1
cnt =0
for i in range(n):
    if arr[i] == element:
        cnt +=1
if cnt > n//2:
    print(element,cnt)
