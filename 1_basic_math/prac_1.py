num = int(input("enter any number"))

while num>0:
    last_digit = num%10
    num = int(num/10)
    print("last_digit",last_digit)

