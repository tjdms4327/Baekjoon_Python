import sys
from math import gcd
input = sys.stdin.readline

x, y, p1, p2 = map(int, input().split())

if (p1 - p2) % gcd(x, y) != 0:
    print(-1)
    sys.exit()
    
limit = max(p1, p2) + x * y
while p1 <= limit and p2 <= limit:
    if p1 == p2:
        print(p1)
        sys.exit()
    elif p1 < p2:
        p1 += x
    else:
        p2 += y
print(-1)
