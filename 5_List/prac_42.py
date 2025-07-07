# Rearrange Array Elements by Sign in alternative sign

arr = [1,-2,3,-4,3,2,-6,-9,5,7,-8,-10]
n= len(arr)

arr1 = [0]*n
#taking 2 indexies withn positive and negative with their starting index
positive,negative = 0,1
for i in range(n):
    if arr[i]>= 0:
        arr1[positive]=arr[i]
        positive += 2
    else:
        arr1[negative]=arr[i]
        negative += 2

print(arr1)