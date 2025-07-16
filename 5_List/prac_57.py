# stock buy and sell: multiple transaction
# Stock Buy and Sell: Multiple Transactions
def stock(arr, n):
    local_min = arr[0]
    local_max = arr[0]
    result = 0
    i = 0

    while i < n - 1:
        # Find local minima (buy point)
        while i < n - 1 and arr[i] >= arr[i + 1]:
            i += 1
        if i == n - 1:
            break
        local_min = arr[i]
        i += 1
        
        # Find local maxima (sell point)
        while i < n and arr[i] >= arr[i - 1]:
            i += 1
        local_max = arr[i - 1]

        result += (local_max - local_min)
    return result


arr = [100, 180, 260, 310, 40, 535, 696]
n = len(arr)
print(stock(arr, n))
