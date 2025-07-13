# moving all the non zeroes in the end of the array

arr = [1,0,2,3,0,0,4,5,0,8,9,0]
n = len(arr)

j = -1
for i in range(0, n):
    if arr[i] == 0:
        j = i   # Pehla zero mila toh j mein store karo
        break    # Break kar do bas pehle zero pe

# Step 2: j ke baad se traverse karna aur non-zero ko swap karna
for i in range(j + 1, n):
    if arr[i] != 0:
        # Non-zero element ko jth index pe bhejna
        arr[i], arr[j] = arr[j], arr[i]
        j += 1  # j ko next zero position pe le jao

# Final answer pr