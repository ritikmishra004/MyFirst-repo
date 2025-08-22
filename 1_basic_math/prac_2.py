#reversing the number

num = int(input("enter any number"))
reverse_num = 0
while num>0:
    last_digit = num%10
    num = int(num/10)
    reverse_num = (reverse_num*10)+last_digit
print ("reverse number",reverse_num)

# sign = 1 if x >= 0 else -1
# x = abs(x)
# reverse_num = 0
# while x:
#     last_digit = x % 10
#     x //= 10
#     reverse_num = (reverse_num * 10) + last_digit
# reverse_num *= sign
# if reverse_num < -2**31 or reverse_num > 2**31 - 1:
#     return 0
            
# return reverse_num