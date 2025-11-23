import sys
input = sys.stdin.readline

n, k = map(int, input().split())
picture = [list(input().split()) for _ in range(n)]

for row in picture:
    x = []
    for i in row:
        x.extend([i] * k)
    for _ in range(k):
        print(*x)