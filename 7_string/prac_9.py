# 451. Sort Characters By Frequency
'''Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.'''


from collections import Counter
s = "tree"
hash_s = Counter(s)
sorted_char = sorted(hash_s.items(), key=lambda x:x[1],reverse=True)
print(hash_s)
result = ''.join(ch * freq for ch, freq in sorted_char)
print(result)