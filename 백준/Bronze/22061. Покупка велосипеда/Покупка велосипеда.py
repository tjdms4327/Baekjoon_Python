# bronzeIII_22061.py
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if b >= c//2:
        c -= (c//2) * 2
    else:
        c -= b*2
    
    
    if c <= a:
        print('YES')
    else:
        print('NO')