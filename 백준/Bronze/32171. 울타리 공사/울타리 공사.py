# bronzeII_32171
import sys
input = sys.stdin.readline

n = int(input())
x1, y1, x2, y2 = 0, 0, 0, 0
for i in range(n):
    if i == 0:
        x1, y1, x2, y2 = map(int, input().split())
    else:
        a, b, c, d = map(int, input().split())
        x1 = min(x1, a)
        y1 = min(y1, b)
        x2 = max(x2, c)
        y2 = max(y2, d)
    
    print((x2-x1 + y2-y1) * 2)