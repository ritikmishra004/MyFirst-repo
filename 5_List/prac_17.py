# intersection of two sorted array

# 🔹 Intersection using sets

arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [2, 4, 6, 8]

# Convert both arrays into sets and take intersection
intersection = list(set(arr1) & set(arr2))

print("Intersection:", sorted(intersection))
print(type(intersection))
