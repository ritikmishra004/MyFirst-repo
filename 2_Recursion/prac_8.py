# pow (x,n)
# linearly

def pow_linear(x, n):
    num = 1
    for i in range(1, abs(n) + 1):
        num = num * x
    return num if n >= 0 else 1 / num

x = 2
n = -3
print(pow_linear(x, n))  # Output: 0.125
