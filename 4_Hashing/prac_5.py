from collections import Counter

# Input array
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

# Frequency count using Counter (shorter than defaultdict)
freq = Counter(arr)

# Display frequency map in sorted order
print("\nFrequencies:")
for num in sorted(freq):
    print(f"{num} -> {freq[num]}")

# Query section
q = int(input("\nEnter number of queries: "))
for _ in range(q):
    number = int(input("Enter number to check frequency: "))
    print(f"Frequency of {number} is {freq[number]}")
