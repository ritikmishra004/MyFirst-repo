# Longest consecutive sequence
# better approach

def pivo(arr,low,high):
    pivot = arr[low]
    i = low+1
    j = high
    while i <= j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >=low and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quick_sort(arr,low, high):
    if low < high:
        partition = pivo(arr,low,high)
        quick_sort(arr,low,partition-1)
        quick_sort(arr,partition+1,high)

arr = [102,4,100,1,101,3,2,1,1,103,104,105,106]
n = len(arr)

# 🟢 Step 1: Sort the array using quick sort
quick_sort(arr, 0, n - 1)
print("Sorted:", arr)

# 🟢 Step 2: Initialize values
longest = 1              # 🔸 answer store karega
current_count = 1        # 🔸 kam se kam ek number to hoga sequence mein
last_smallest = arr[0]   # 🔸 pehle element se sequence start

# 🟢 Step 3: Loop over sorted array to find longest consecutive
for i in range(1, n):
    # ✅ Consecutive number mila → count badhao
    if arr[i] - 1 == last_smallest:
        current_count += 1
        last_smallest = arr[i]

    # 🔁 Duplicate number mila → ignore karo
    elif arr[i] == last_smallest:
        continue

    # ❌ Sequence break ho gaya → naya sequence start karo
    else:
        current_count = 1
        last_smallest = arr[i]
    
    # 🔃 Har step pe longest update karo
    longest = max(longest, current_count)

# ✅ Final Output
print("Longest Consecutive Length:", longest)
