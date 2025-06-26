# Merge sort

def merge_sort(arr,low,high):
    
    if low >= high:
        return
    mid = (low + high)//2

    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    temp = []
    left = low
    right = mid+1
    while left <=mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
# important and confusing
    for i in range(low, high + 1):  
    # 🔹 i loop karega low se high tak (inclusive)
    # 🔹 Python mein range ka end exclusive hota hai, isiliye high+1 likha gaya hai
    # 🔹 Ye loop original array ke us portion ko cover karega jahan sorted data wapas daalna hai

        arr[i] = temp[i - low]  
        # 🔹 temp ek naya list hai jisme sorted elements hain (temp[0], temp[1], ..., temp[n])
        # 🔹 i - low ka matlab hai: temp ka index 0 se shuru hota hai, jabki arr mein insert low se
        # 🔹 Example: agar low = 2 aur i = 2, to temp[0] → arr[2]
        # 🔹 Har temp element ko uski actual position (original array mein) mein daala jaa raha hai


arr = list(map(int,input("Enter numbers : ").split()))
n = len(arr)
merge_sort(arr,0,n-1)

print("Sorted array : ",arr)