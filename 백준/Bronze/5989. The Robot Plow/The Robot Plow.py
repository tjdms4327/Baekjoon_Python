import sys
input = sys.stdin.readline

X, Y, I = map(int, input().split())

matrix = [[0]*(Y+1) for _ in range(X+1)]
for _ in range(I):
    x0, y0, x1, y1 = map(int, input().split())
    for row in range(x0, x1+1):
        for col in range(y0, y1+1):
            matrix[row][col] = 1

print(sum(row.count(1) for row in matrix))