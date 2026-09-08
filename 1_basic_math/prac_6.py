# all divisors 
num = int(input("Enter any number"))

for i in range (1,num+1):
    if (num%i == 0):
        print(i, end = " ")
