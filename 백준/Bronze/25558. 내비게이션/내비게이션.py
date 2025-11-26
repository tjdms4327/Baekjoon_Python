import sys
input = sys.stdin.readline

n = int(input())
sx, sy, ex, ey = map(int, input().split())

D = [0]
for _ in range(n):
    m = int(input())
    d = 0
    x0, y0 = sx, sy
    for _ in range(m):
        x, y = map(int, input().split())
        d += abs(x0-x)+abs(y0-y)
        x0, y0 = x, y
    d += abs(ex-x0)+abs(ey-y0)
    D.append(d)

print(D.index(min(D[1:])))