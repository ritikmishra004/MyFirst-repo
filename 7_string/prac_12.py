# 8. String to Integer (atoi)
#  not done yet

def stringTointeger(s):
        s = s.strip()
        if not s:
                return 0
        sign = 1   # ✅ By default positive
        index = 0  # ✅ Starting index 0 se

        # ✅ Step 2: Check '+' or '-'
        if s[0] == '-':
                sign = -1
                index += 1  # '-' ya '+' mil gaya to index aage badhao
        elif s[0] == '+':
                index += 1

        num = 0  # ✅ Final number banane ke liye
                # ✅ Step 3: Jab tak digits milte rahe tab tak number banao
        while index < len(s) and s[index].isdigit():
                num = num * 10 + int(s[index])  # Old number ko 10x karke naya add karo
                index += 1
                
        num *= sign  # ✅ Step 4: Sign laga do (positive/negative)

                # ✅ Step 5: Clamp 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
                
        if num < INT_MIN:
                return INT_MIN
        if num > INT_MAX:
                return INT_MAX
                
        return num

s = " -042"
print(stringTointeger(s))