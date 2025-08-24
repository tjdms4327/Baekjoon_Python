import sys
input = sys.stdin.readline

d1, d2, d3 = map(int, input().split())
b = (d1 + d3 - d2) / 2
a = d1 - b
c = d3 - b

if a>0 and b>0 and c>0:
    print(1)
    print(f'{a:.1f} {b:.1f} {c:.1f}')
else: 
    print(-1)