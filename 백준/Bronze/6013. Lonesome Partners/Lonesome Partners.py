import sys
input = sys.stdin.readline

n = int(input())
cow = [tuple(map(int, input().split())) for _ in range(n)]

best = 0
for i in range(n):
    x0, y0 = cow[i]
    for j in range(i+1, n):
        x1, y1 = cow[j]
        dist2 = (x0-x1)**2 + (y0-y1)**2
        if best < dist2:
            best = dist2
            idx = [i+1, j+1]
print(*idx)