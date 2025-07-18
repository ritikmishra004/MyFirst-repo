# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Input: s = "anagram", t = "nagaram"
# Output: true
from collections import Counter
s = "anagram"
t = "nagaram"

hash_s = Counter(s)
hash_t = Counter(t)

if hash_s == hash_t:
    print(True)
else:
    False