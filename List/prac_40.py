# Best time to buy and sell stocks

arr = [7,1,5,3,6,4]
n = len(arr)

profit = 0
mini = arr[0]
for i in range(1,n):
    cost = arr[i] - mini
    profit = max(profit,cost)
    mini = min(mini,arr[i])

print(profit)