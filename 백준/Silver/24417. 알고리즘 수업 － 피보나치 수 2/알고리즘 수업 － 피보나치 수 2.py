import sys
input = sys.stdin.readline

MOD = 1000000007

n = int(input())

def fib(n):
    if n == 0:
        return (0, 1)
    a, b = fib(n // 2)
    c = (a * ((2 * b - a) % MOD)) % MOD
    d = (a * a + b * b) % MOD
    
    if n % 2 == 0:
        return (c, d)
    else:
        return (d, (c + d) % MOD)


fn = fib(n)[0] % MOD
print(fn, (n - 2) % MOD)