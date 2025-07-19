# 1781. Sum of Beauty of All Substrings
# Input: s = "aabcb"
# Output: 5
def substring(s):
    n =len(s)
    summ_of_string = 0
    for i in range(n):
        hash_map = {}*26
        if i in hash_map:
            hash_map[i] +=1
        else:
            hash_map[i] = 1
        for j in range(0,len(hash_map)):
            pass

s = "aabcb"
print(substring(s))