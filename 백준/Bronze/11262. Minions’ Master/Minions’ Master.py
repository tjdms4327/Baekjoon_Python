import sys
input = sys.stdin.readline
from decimal import Decimal, ROUND_HALF_UP

t = int(input())
for _ in range(t):
    n, *strengths = map(int, input().split())
    
    s = sum(strengths)
    avg = Decimal(s) / Decimal(n)
    
    higher = sum(1 for x in strengths if x*n > s)
    prop = Decimal(higher*100) / Decimal(n)

    avg = avg.quantize(Decimal("0.000"), rounding=ROUND_HALF_UP)
    prop = prop.quantize(Decimal("0.000"), rounding=ROUND_HALF_UP)
    print(f"{avg} {prop}%")