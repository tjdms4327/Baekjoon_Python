import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(input().strip()) for _ in range(n)]

d = [
    (1,1),(1,-1),(1,0),
    (0,1),(0,-1),
    (-1,1),(-1,-1),(-1,0)
]

ans = [[0]*n for _ in range(n)]
for r in range(n):
    for c in range(n):
        if matrix[r][c] != '.':
            ans[r][c] = '*'  # 지뢰
            cnt = int(matrix[r][c])
            
            for dx, dy in d:
                nx = r + dx
                ny = c + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if isinstance(ans[nx][ny], int):
                        ans[nx][ny] += cnt
                        if ans[nx][ny] >= 10:
                            ans[nx][ny] = 'M'

for row in ans:
    print(''.join(str(x) for x in row))