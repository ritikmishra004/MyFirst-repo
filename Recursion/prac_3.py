def func(i,n):
    if i >= n // 2:
        return
    # swapping elements
    temp = arr[i]
    arr[i] = arr[n - i - 1]
    arr[n - i - 1] = temp

    func(i + 1,n)  # recursive call

arr = [1, 2, 3, 4, 5]
n = len(arr)
func(0,n)
print(arr)
