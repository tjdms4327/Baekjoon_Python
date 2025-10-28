# bronzeI_14647
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [input().split() for _ in range(n)]

max9 = -1
tot9 = 0
for row in matrix:
    row_count = sum(cell.count('9') for cell in row)
    max9 = max(max9, row_count)
    tot9 += row_count
for col in zip(*matrix):
    col_count = sum(cell.count('9') for cell in col)
    max9 = max(max9, col_count)

print(tot9 - max9)