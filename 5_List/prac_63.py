# Maximum Product Subarray
# not done yet
def maximum_product(arr,n):
    max_product = float('-inf')
    lefttoright = 1
    righttoleft = 1

    for i in range(n):
        if lefttoright == 0:
            lefttoright = 1
        if righttoleft == 0:
            righttoleft = 1

        # calculate product from index left to right
        lefttoright *= arr[i]

        # calculate product from index right to left
        j = n - i - 1
        righttoleft *= arr[j]
        max_product = max(lefttoright, righttoleft, max_product)
    
    return max_product

arr = [-2, 6, -3, -10, 0, 2]
n = len(arr)
print(maximum_product(arr,n))