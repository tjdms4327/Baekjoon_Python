import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for _ in range(q):
    line = list(map(int, input().split()))
    
    if line[0] == 0:
        i, j, k = line[1:]
        matrix[i][j] = k
    else:
        i, j = line[1:]
        matrix[i], matrix[j] = matrix[j], matrix[i]
        
for row in matrix:
    print(*row)