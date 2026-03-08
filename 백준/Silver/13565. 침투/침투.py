import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(m)]

queue = deque()
visited = [[False]*n for _ in range(m)]
for i in range(n):
    if grid[0][i] == 0:
        queue.append((0,i))
        visited[0][i] = True
        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
        
while queue:
    x, y = queue.popleft()
    
    if x == m-1:
        print('YES')
        sys.exit()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<m and 0<=ny<n:
            if not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
                
print('NO')