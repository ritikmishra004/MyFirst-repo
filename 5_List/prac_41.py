# Rearrange Array Elements by Sign in alternative sign

arr = [1,-2,3,-4,3,2,-6,-9,5,7,-8,-10]
n= len(arr)
positive = []
negative = []

for i in range(n):
    if arr[i]>=0:
        positive.append(arr[i])
    else:
        negative.append(arr[i])

print(positive,"\n",negative)

for i in range(0,n//2):
    arr[2*i]= positive[i]
    arr[2*i+1] = negative[i]

print(arr)