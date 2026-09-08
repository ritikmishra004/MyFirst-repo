s = input("Enter any string: ").lower()

# 26 size list for a to z
hashh = [0] * 26

# Count frequency of each lowercase character
for ch in s:
    index = ord(ch) - ord('a')   # converts 'a' to 0, 'b' to 1, ..., 'z' to 25
    if 0 <= index < 26:          # ensure it’s a lowercase letter
        hashh[index] += 1

q = int(input("Enter the no. of queries : "))
for i in range(q):
    ch = input("Enter character : ")                 # Ask for character to check
    index = ord(ch) - ord('a')                       # Get its index
    if 0 <= index < 26:
        print(f"{ch} occurs {hashh[index]} times")   # Print its frequency
    else:
        print("Invalid character. Please enter lowercase a-z only.")