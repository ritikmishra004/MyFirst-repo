# Insertion sort

arr = list(map(int, input("Enter numbers : ").split()))
n = len(arr)

# i = 1 se shuru hota hai, kyunki index 0 ka element already sorted maana jaata hai
for i in range(1, n):

    key = arr[i]          # key = current element jise sorted left part mein insert karna hai
    j = i - 1             # j = key ke pehle wale index pe point karta hai (left side)

    # Shift elements of arr[0..i-1], that are > key
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]  # shift right
        j -= 1               ## Pichle element pe move kar jao (left check karne ke liye)

    arr[j + 1] = key      # Jahan j ruk gaya uske next index pe key ko insert karo

print("Sorted array:", arr)
