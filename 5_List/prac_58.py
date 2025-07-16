def stock(arr,n):
    result = 0
    
    for i in range(n-1):
        if arr[i]<arr[i+1]:
            result += arr[i+1]-arr[i]
    return result


arr = [100, 180, 260, 310, 40, 535, 695]
n = len(arr)
print(stock(arr, n))