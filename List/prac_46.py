# leader in an array : on their right everyone should be smaller than that number 
# optimal approach

import sys

arr = [10, 22, 12, 4, 3, 0, 6]
n = len(arr)

leader = []
mini = -sys.maxsize

# 🔁 Step 1: Right to Left traversal karna padega
# kyunki leader hamesha apne right ke sabhi elements se bada hota hai
for i in range(n - 1, -1, -1):  # i = n-1 to 0
    # Step 2: Agar current element mini se bada hai
    # to wo ek leader hai, kyunki uske right mein koi usse bada nahi
    if arr[i] > mini:
        leader.append(arr[i])  
        mini = max(mini,arr[i])         

print(leader)
