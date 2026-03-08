import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


queue = deque()
dist = [[-1]*m for _ in range(n)]
for r in range(n):
    for c in range(m):
        if grid[r][c] == 1:
            queue.append((r, c))
            dist[r][c] = 0
            
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
while queue:
    x, y = queue.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<m:
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
                
print(max(map(max, dist)))          