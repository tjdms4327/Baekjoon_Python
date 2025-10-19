# bronzeI_1236
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]

add_row, add_col = 0, 0
for row in matrix:
    if 'X' not in row:
        add_row += 1
for col in zip(*matrix):
    if 'X' not in col:
        add_col += 1

print(max(add_row, add_col))