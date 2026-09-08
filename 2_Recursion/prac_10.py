# reversing the array using recursion

def rec_reverse(i,n):
    if i >= n//2:
        return
    temp = arr[i]
    arr[i] = arr[n-i-1]
    arr[n-i-1] = temp
    rec_reverse(i+1,n)


arr = [4,5,6,7,8,9]
n = len(arr)
rec_reverse(0,n)
print(arr)