# 🔍 Linear search: check each element one by one
def linear_search(arr, search, n):
    for i in range(n):                       # 🔁 Loop from 0 to n-1
        if search == arr[i]:                # ✅ Match found
            return f"Found at index {i}"
    return "Not found"                      #  No match found

# 🔹 Driver code
arr = [4, 5, 2, 5, 3, 7, 8, 43, 90]
n = len(arr)
search = int(input("Enter number to search: "))
print(linear_search(arr, search, n))
