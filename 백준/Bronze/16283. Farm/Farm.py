import sys
input = sys.stdin.readline

a, b, n, w = map(int, input().split())

result = []
for i in range(1, n):
    x, y = i, n-i
    if a*x+b*y == w:
        result.append((x,y))

if len(result)==1:
    print(*result[0])
else:
    print(-1)