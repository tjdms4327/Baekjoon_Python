import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


distance = [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i, j)
        if graph[i][j] in [0, 2]:
            distance[i][j] = 0


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
q.append(start)
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]==1 and distance[nx][ny]==-1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))
                
              
for row in distance:
    print(*row)  