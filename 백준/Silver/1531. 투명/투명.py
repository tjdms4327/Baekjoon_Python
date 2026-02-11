import sys
input = sys.stdin.readline

n, m = map(int, input().split())

picture = [[0]*100 for _ in range(100)]
for _ in range(n):
    x0, y0, x1, y1 = map(int, input().split())
    for y in range(y0-1, y1):
        for x in range(x0-1, x1):
            picture[x][y] += 1

tot = 0
for row in picture:
    tot += sum(1 for x in row if x > m)
print(tot)