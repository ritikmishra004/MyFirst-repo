# finding second largest number
# brute force approach


# for partition and pivot element
def piv(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i],arr[j]=arr[j],arr[i]

    arr[low],arr[j]=arr[j],arr[low]
    return j

# quick sort algo:
def quick_sort(arr,low,high):
    if low<high:
        partition = piv(arr,low, high)
        quick_sort(arr,low,partition-1)
        quick_sort(arr,partition+1,high)


arr = list(map(int,input("Enter numbers : ").split()))
n = len(arr)
quick_sort(arr,0,n-1)

for i in range(n-2,0,-1):
    largest = arr[n-1]
    if arr[i] != largest:
        largest = arr[i]
        break

print("second largest number : ",largest)