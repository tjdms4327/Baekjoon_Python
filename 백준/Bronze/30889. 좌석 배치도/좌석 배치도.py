import sys
input = sys.stdin.readline

matrix = [['.']*20 for _ in range(10)]

n = int(input())
for _ in range(n):
    s = input().strip()
    row, col = ord(s[0])-ord('A'), int(s[1:])-1
    matrix[row][col] = 'o'
for row in matrix:
    result = ''.join(row)
    print(result)