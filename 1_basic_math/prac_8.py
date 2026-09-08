# greatest common divisor
# Highest common factor

n1 = int(input ("Enter any number "))

n2 = int(input("Enter any number "))

while (n1>0 and n2>0):
    if (n1>n2):
        n1=n1%n2
    else:
        n2 = n2%n1
if n1==0:
    gcd=n2
else:
    gcd = n1
print (gcd)