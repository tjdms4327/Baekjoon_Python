# bronzeI_23841
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]

for i in range(m//2):
    for row in range(n):
        if matrix[row][i] != '.':
            matrix[row][m-1-i] = matrix[row][i]
        elif matrix[row][m-1-i] != '.':
            matrix[row][i] = matrix[row][m-1-i]

for row in matrix:
    print(''.join(row))