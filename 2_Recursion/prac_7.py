# myAtoi
# "   -42" into integer -42

def myAtoi(s):
    s = s.lstrip()
    if not s:
        return 0
    
    sign = 1
    index = 0
    if s[0]=='-':
        sign = -1
        index += 1
    elif s[0] == '+':
        index += 1
    
    def read_digit(index,num):
        if index >= len(s) or not s[index].isdigit():
            return num
        num = num*10+int(s[index])
        return read_digit(index+1,num)
    number = read_digit(index,0)*sign

    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    if number < INT_MIN:
        return INT_MIN
    if number > INT_MAX:
        return INT_MAX
    return number

# Example run
print(myAtoi("42"))        # 42
print(myAtoi("   -042"))   # -42
