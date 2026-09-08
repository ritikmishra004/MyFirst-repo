# Maximum Product Subarray
def maximum_product(arr,n):
    max_product = arr[0]
    
    for i in range(n):
        product = 1
        for j in range(i+1,n):
            product *= arr[j]
            max_product = max(max_product,product)
    return max_product
arr = [-2, 6, -3, -10, 0, 2]
n = len(arr)
print(maximum_product(arr,n))