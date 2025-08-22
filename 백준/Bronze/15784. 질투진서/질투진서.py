import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

Jinseo = matrix[a-1][b-1]
for i in matrix[a-1]:
    if i > Jinseo:
        print('ANGRY')
        exit(0)
for i in range(n):
    if matrix[i][b-1] > Jinseo:
        print('ANGRY')
        exit(0)
print('HAPPY')