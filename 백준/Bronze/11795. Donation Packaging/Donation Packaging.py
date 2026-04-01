# bronzeIII_11795
import sys
input = sys.stdin.readline

a, b, c = 0, 0, 0
t = int(input())
for _ in range(t):
    a0, b0, c0 = map(int, input().split())
    a += a0 ; b += b0 ; c += c0
    
    if min(a, b, c) < 30:
        print('NO')
    else:
        set0 = min(a, b, c)
        print(set0)
        a -= set0 ; b -= set0 ; c -= set0