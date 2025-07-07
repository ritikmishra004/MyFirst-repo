# Armstrong 

num = int(input("Enter any number"))
sum = 0
num_2 = num
while num>0:
    last_digit = num%10
    num =int(num/10)
    sum = sum+ (last_digit*last_digit*last_digit)
    
print (sum)
if num_2 == sum:
    print("it is an armstrong")
else:
    print("it is not an armstrong")