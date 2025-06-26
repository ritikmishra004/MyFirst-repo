# Quick sort 
def piv(arr, low, high):
    pivot = arr[low]  # choose the pivot element (first element)

    i = low
    j = high

    while i < j:
        # move i forward until we find an element greater than pivot
        while i <= high and arr[i] <= pivot:
            i += 1

        # move j backward until we find element less than or equal to pivot
        while j >= low and arr[j] > pivot:
            j -= 1

        # swap only if i < j
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # put pivot at its correct sorted position
    arr[low], arr[j] = arr[j], arr[low]
    return j  # partition index

def quick_sort(arr, low, high):
    if low < high:
        partition = piv(arr, low, high)
        quick_sort(arr, low, partition - 1)
        quick_sort(arr, partition + 1, high)

# Driver code
arr = list(map(int, input("Enter numbers: ").split()))
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
