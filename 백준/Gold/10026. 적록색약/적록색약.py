import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
grid = [list(input().strip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False]*n for _ in range(n)]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    color = grid[x][y]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and grid[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    
count = 0 # 정상시야
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count += 1
                
                
visited2 = [[False]*n for _ in range(n)]
def bfs2(x, y):
    queue = deque()
    queue.append((x, y))
    visited2[x][y] = True
        
    color = grid[x][y]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
                
            if 0<=nx<n and 0<=ny<n:
                if not visited2[nx][ny]:
                    cand_color = grid[nx][ny]
                    if cand_color == color or (cand_color in 'RG' and color in 'GR'):
                        visited2[nx][ny] = True
                        queue.append((nx, ny))
                    
count2 = 0 # 적록색맹
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            bfs2(i, j)
            count2 += 1
                
                
print(count, count2)