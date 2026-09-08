# largest number

def quick_sort(arr,low,high):
    if low < high:
        partition = piv(arr,low,high)
        quick_sort(arr,low,partition-1)
        quick_sort(arr,partition+1,high)

def piv(arr,low,high):
    pivot = arr[low]
    
    i = low
    j = high
    while i < j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j]> pivot:
            j -= 1
        if i < j:
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[low],arr[j]=arr[j],arr[low]
    return j

arr = [5,43,8,23,5,98,33,8]
# this is also the way to find largest element
# it find the element without sorting
print("largest element : ",max(arr))

# and the other one
quick_sort(arr,0,len(arr)-1)
print("largest element : ",arr[-1])