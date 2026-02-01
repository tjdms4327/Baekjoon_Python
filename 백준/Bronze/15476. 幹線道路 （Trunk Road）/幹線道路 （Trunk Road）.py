import sys
input = sys.stdin.readline

r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]

cand = []
for row in range(r):
    for col in range(c):
        cur = sum(matrix[i][j] * min(abs(row-i), abs(col-j)) \
                    for i in range(r) for j in range(c))
        cand.append(cur)

print(min(cand))