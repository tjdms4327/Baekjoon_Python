import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
water = [int(input()) for _ in range(n-1)]

if a not in water and b not in water:
    print(-1)
elif a not in water:
    print(a)
elif b not in water:
    print(b)
else:
    print(*range(a, b+1), sep='\n')