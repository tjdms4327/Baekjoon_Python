import sys
input = sys.stdin.readline

n, m, d = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]

count = 0
for row in matrix:
    for c in range(0, m-d+1):
        if '#' not in row[c:c+d]:
            count += 1
for col in zip(*matrix):
    col = list(col)
    for r in range(0, n-d+1):
        if '#' not in col[r:r+d]:
            count += 1
print(count)