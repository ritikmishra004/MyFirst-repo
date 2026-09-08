class Solution:
    def reverseWords(self, s: str) -> str:
        # ✅ Step 1: s.split() se multiple spaces hat jaati hain aur words mil jaate hain
        # ' '.join() se ek hi space ke saath string ban gayi
        str_corr = " ".join(s.split())

        # ✅ Step 2: Phir us string ko list bana liya jisme words alag-alag hain
        str_ls = str_corr.split()   # ['the', 'sky', 'is', 'blue'] jaisa

        # ✅ Step 3: Two pointer approach se reverse karenge
        i = 0
        j = len(str_ls) - 1  # End of list se shuru

        while i < j:
            # Swap karna words ko left <-> right
            str_ls[i], str_ls[j] = str_ls[j], str_ls[i]
            i += 1
            j -= 1

        # ✅ Step 4: Reverse ho gaya, ab ek hi space ke saath wapas string bana do
        return " ".join(str_ls)
