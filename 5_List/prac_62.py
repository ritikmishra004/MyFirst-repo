# Maximum Product Subarray

def maximum_product(arr,n):
    cur_min = arr[0]
    cur_max = arr[0]
    result = arr[0]

    for i in range(1,n):
        num = arr[i]

        if arr[i]<0:
            cur_max,cur_min = cur_min,cur_max
        
        cur_max = max(num,num*cur_max)
        cur_min = min(num,num*cur_min)
        result = max(result,cur_max)
    return result

arr = [-2, 6, -3, -10, 0, 2]
n = len(arr)
print(maximum_product(arr,n))