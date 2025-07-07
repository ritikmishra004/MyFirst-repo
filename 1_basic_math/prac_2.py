#reversing the number

num = int(input("enter any number"))
reverse_num = 0
while num>0:
    last_digit = num%10
    num = int(num/10)
    reverse_num = (reverse_num*10)+last_digit
print ("reverse number",reverse_num)
