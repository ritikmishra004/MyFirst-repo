# # 13. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,}

s = "LVC"
total = 0
prev = 0
for ch in reversed(s):
    curr = roman[ch]
    if curr < prev:
        total -= curr
    else:
        total += curr
    prev = curr
print(total)