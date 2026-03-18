import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

cnt = 0
visited = [[False]*n for _ in range(m)]
for r in range(m):
    for c in range(n):
        if grid[r][c]==1 and not visited[r][c]:
            queue = deque([(r,c)])
            visited[r][c] = True
            
            while queue:
                x, y = queue.popleft()
                
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if 0<=nx<m and 0<=ny<n:
                        if not visited[nx][ny] and grid[nx][ny]==1:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            
            cnt += 1
    
print(cnt)