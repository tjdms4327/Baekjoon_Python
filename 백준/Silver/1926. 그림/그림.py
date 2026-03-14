import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
painting = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

W = []
visited = [[False]*m for _ in range(n)]
for r in range(n):
    for c in range(m):
        if not visited[r][c] and painting[r][c]==1:
            queue = deque([(r, c)])
            visited[r][c] = True
            w = 1
            
            while queue:
                x, y = queue.popleft()
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if 0<=nx<n and 0<=ny<m:
                        if not visited[nx][ny] and painting[nx][ny]==1:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            w += 1
            
            W.append(w)
            
if W:
    print(len(W))    
    print(max(W))
else:
    print(0)
    print(0)