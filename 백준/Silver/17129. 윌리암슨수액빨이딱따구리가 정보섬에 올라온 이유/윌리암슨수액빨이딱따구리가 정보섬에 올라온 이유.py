import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
A = []
for i in range(n):
    row = list(map(int, input().strip()))
    A.append(row)
    if 2 in row:
        start = (i, row.index(2), 0)
        
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
        
queue = deque([start])
visited = [[False]*m for _ in range(n)]
visited[start[0]][start[1]] = True

while queue:
    x, y, cnt = queue.popleft()
    
    if A[x][y] in [3, 4, 5]:
        print('TAK')
        print(cnt)
        sys.exit()
        
    for d1, d2 in zip(dx, dy):
        nx = d1 + x
        ny = d2 + y
        
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and A[nx][ny]!=1:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt+1))
                
print('NIE')