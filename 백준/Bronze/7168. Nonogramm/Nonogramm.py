import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [input().strip() for _ in range(n)]

for row in matrix:
    if set(row) == set('.'):
        print(0)
    else:
        result = list(map(len, row.split('.')))
        print(*[x for x in result if x != 0])
for col in zip(*matrix):
    if set(col) == set('.'):
        print(0)
    else:
        result = list(map(len, ''.join(col).split('.')))
        print(*[x for x in result if x != 0])