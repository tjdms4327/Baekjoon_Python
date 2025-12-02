import sys
input = sys.stdin.readline

n, m = map(int, input().split())

box = list(range(n+1))
for _ in range(m):
    x, y = map(int, input().split())
    box[x] = y
print(*box[1:], sep='\n')