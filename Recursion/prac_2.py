# Functional

def sum(n):
    if n==0 :
        return 0
    return n + sum (n-1)

n = int(input("Enter any number"))
print("sum is",sum(n))