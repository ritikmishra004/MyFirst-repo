# Selection sort

arr = list(map(int, input("Enter elements: ").split()))

n = len(arr)

for i in range(n):
    minn = i
    for j in range(i + 1, n):
        if arr[j] < arr[minn]:
            minn = j
    temp = arr[i]
    arr[i] = arr[minn]
    arr[minn] = temp

print(f"The sorted array is : {arr}")