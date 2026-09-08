# power(x,n)

def pow(x, n):
    # Base case
    if n == 0:
        return 1
    if n < 0:
        return 1 / pow(x, -n)  # handle negative power
    
    # Recursive case
    return x * pow(x, n - 1)

# Test
x = 2
n = 3
print(pow(x, n))   # 8
print(pow(2, -3))  # 0.125
