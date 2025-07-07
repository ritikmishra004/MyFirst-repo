# fibonaci
def fibo(n):
    if (n<=1):
        return n
    return (fibo(n-1)+fibo(n-2))

n = 9
print(fibo(n))
