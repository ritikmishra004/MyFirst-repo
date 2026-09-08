# Function to calculate the maximum profit
def maximumProfit(prices):
    n = len(prices)
    lMin = prices[0]  # Local Minima
    lMax = prices[0]  # Local Maxima
    res = 0

    i = 0
    while i < n - 1:
        # Find local minima
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        lMin = prices[i]
        
        # Local Maxima
        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
        lMax = prices[i]

        # Add current profit
        res += (lMax - lMin)

    return res


prices = [100, 180, 260, 310, 40, 535, 695]
print(maximumProfit(prices))