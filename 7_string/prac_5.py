# 14. Longest Common Prefix


def longestCommonPrefix(strs):
        if not strs:
            return ""  # ✅ Agar list khali hai

        prefix = strs[0]  # ✅ Pehli string ko base bana lo

        for s in strs[1:]:  # ✅ Baaki sab string ke sath compare karo
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # ✅ Har baar ek character peeche se kaato
                if not prefix:
                    return ""  # ✅ Koi common nahi mila to empty string
        
        return prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))