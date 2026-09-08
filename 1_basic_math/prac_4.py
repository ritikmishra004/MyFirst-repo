#palindrome

num = int(input("enter any number"))
num_2 = num
reverse_num = 0

while num>0:
    last_digit = num%10
    num = int(num/10)
    reverse_num = (reverse_num*10)+last_digit
print ("reverse number",reverse_num)

if reverse_num == num_2:
    print("its a palindrome")
else:
    print("it is not palindrome")
