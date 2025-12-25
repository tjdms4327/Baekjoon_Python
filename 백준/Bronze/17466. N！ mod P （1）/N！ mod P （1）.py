import sys
input = sys.stdin.readline

n, p = map(int, input().split())

prod = 1
for i in range(n+1, p):
    prod = (prod * i) % p
    
inv = pow(prod, p-2, p)
result = (-inv) % p
print(result)
