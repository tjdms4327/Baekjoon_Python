# bronzeI_16433
import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
r = (r - 1) % 2 ; c = (c - 1) % 2

matrix = [['.' for _ in range(n)] for _ in range(n)]
for row in range(n):
    for col in range(n):
        if (row%2 != r and col%2 != c) or (row%2 == r and col%2 == c):
            matrix[row][col] = 'v'

for row in matrix:
    print(''.join(row))