import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
price_package, price_per = float('inf'), float('inf')
for _ in range(m):
    a, b = map(int, input().split())
    price_package = min(price_package, a)
    price_per = min(price_per, b)

cand = [n*price_per, math.ceil(n/6)*price_package, (n//6)*price_package+(n%6)*price_per]
print(min(cand))