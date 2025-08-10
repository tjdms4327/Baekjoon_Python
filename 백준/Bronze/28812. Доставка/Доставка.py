import sys
input=sys.stdin.readline

n,c=map(int, input().split())
min_price=float('inf')
for _ in range(n):
    p,d,v=map(int, input().split())
    price=p+d+v*c
    if min_price>price:
        min_price=price
print(min_price)