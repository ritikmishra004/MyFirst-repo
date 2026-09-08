s = input("Enter a string: ")   # Example: "applebanana"

char_freq = {}

for ch in s:
    if ch in char_freq:
        char_freq[ch] += 1
    else:
        char_freq[ch] = 1

# Check frequency
query = input("Enter character to check frequency: ")
print(f"'{query}' occurs {char_freq.get(query, 0)} times.")
