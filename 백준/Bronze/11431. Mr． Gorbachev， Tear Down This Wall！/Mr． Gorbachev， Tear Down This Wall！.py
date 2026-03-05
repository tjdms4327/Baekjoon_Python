import sys
input = sys.stdin.readline
import math

t = int(input())
for case in range(1, 1+t):
    n, s, p = map(int, input().split())
    xy = [tuple(map(int, input().split()))for _ in range(n+1)]
    
    tot = 0
    for i in range(0, n):
        x0, y0 = xy[i]
        x1, y1 = xy[i+1]
        tot += abs(x1-x0) + abs(y1-y0)
    
    tot *= s
    print(f'Data Set {case}:\n{math.ceil(tot/p)}\n')