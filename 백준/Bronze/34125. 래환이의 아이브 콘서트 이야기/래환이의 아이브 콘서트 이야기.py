# bronzeIII_34125
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

if all(all(x == 1 for x in row) for row in matrix):
    print(-1)
    exit()

min_d = float('inf')
r, c = -1, -1
for row in range(n):
    for col in range(m):
        if matrix[row][col] == 1:
            continue
        d = (row + 1) + abs((m + 1) // 2 - (col + 1))
        if d < min_d:
            min_d = d
            r, c = row + 1, col + 1
print(r, c)