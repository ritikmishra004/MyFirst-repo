# majority Element greator than n/2

arr = [2,2,3,2,2,4,2,2,3,2,3,4,5,2,5]
n= len(arr)

for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[i]==arr[j]:
            cnt += 1
        
    if cnt > n//2:
        print (arr[i],cnt)
        break
else:
    print("not valid")