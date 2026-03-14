import sys
input = sys.stdin.readline
from collections import deque

m, n, k = map(int, input().split())

grid = [[True]*n for _ in range(m)]
for _ in range(k):
    x0, y0, x1, y1 = map(int, input().split())
    for y in range(y0, y1):      
        for x in range(x0, x1):
            grid[y][x] = False
            
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
            
area = []
visited = [[False]*n for _ in range(m)]
for r in range(m):
    for c in range(n):
        if grid[r][c] and not visited[r][c]:
            queue = deque([(r, c)])
            visited[r][c] = True
            a = 1
            
            while queue:
                x, y = queue.popleft()
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if 0<=nx<m and 0<=ny<n:
                        if not visited[nx][ny] and grid[nx][ny]:
                            a += 1
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            
            area.append(a)
            
            
print(len(area))
print(*sorted(area))