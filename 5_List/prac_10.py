# rotate an array by k numbers
def rotate(arr,d):
    # Step 1: Reverse first d elements
    arr[:d] = reversed(arr[:d])                   

    # Step 2: Reverse remaining n-d elements
    arr[d:] = reversed(arr[d:])

    # Step 3: Reverse entire array
    arr[:] = reversed(arr)

    return arr
arr = list(map(int, input("Enter numbers: ").split()))
n =len(arr)
d = int(input("Enter any number : "))
d = d%n
rotate(arr,d)
print("rotated array",arr)


# arr[:d] = arr[:d][::-1]
# arr[d:] = arr[d:][::-1]
# arr[:]  = arr[::-1].  arr[::-1] returns a new reversed list, so use """"arr[:] =""""
                        #  to copy back into original array.

# arr[:d:-1]      # ❌ This line does nothing because you didn't assign it
# arr[d::-1]      # ❌ Same issue — result is created but not used
# arr[::-1]       # ❌ Again, slicing creates a new list but isn't saved back
# return arr