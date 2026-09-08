# 5. Longest Palindromic Substring
'''Input: s = "babad"
    Output: "bab"
Explanation: "aba" is also a valid answer.'''

def palindrom(s):
        # ✅ Edge case agar 1 ya empty ho to return khud ko
        if len(s) <= 1:
            return s
        
        res = ""  # ✅ Final answer yaha store hoga
        
        # ✅ Expand function banayenge ek center se left/right check karne ke liye
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]  # ✅ Palindrome substring return hogi
        
        # ✅ Har index pe odd & even dono tarah expand karenge
        for i in range(len(s)):
            temp1 = expand(i, i)     # ✅ Odd length center
            temp2 = expand(i, i + 1) # ✅ Even length center
            
            # ✅ Jo bada hoga usko store karenge
            if len(temp1) > len(res):
                res = temp1
            if len(temp2) > len(res):
                res = temp2
        
        return res
s = "babad"
print(palindrom(s))
