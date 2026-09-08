# intersection 
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 3, 3]

# 'visited' list arr2 ke elements ke liye banai gayi hai
#   Iska use hoga taaki hum same element ko dubara match na karen
visited = [0] * len(arr2)
intersection = []
for i in range(len(arr1)):

    for j in range(len(arr2)):
        if arr1[i] == arr2[j] and visited[j] == 0:

            # Match mil gaya → intersection list me add karo
            intersection.append(arr1[i])
            visited[j] = 1    # Is element ko mark kar do taaki dobara use na ho

            break            # Break karte hain taaki ek arr1[i] sirf ek arr2[j] se hi match kare
print("Intersection (with duplicates):", intersection)