import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

rgb = [[] for _ in range(n)]
for j in range(n):
    line = list(map(int, input().split()))
    for i in range(0, 3*m, 3):
        r, g, b = line[i:i+3]
        rgb[j].append(r+g+b)
        
t3 = 3 * int(input())

object = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if rgb[i][j] >= t3:
            object[i][j] = 1
            
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
            
cnt = 0
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if object[i][j] == 1 and not visited[i][j]:
            cnt += 1
            queue = deque([(i, j)])
            visited[i][j] = True
            
            while queue:
                x, y = queue.popleft()
                
                for d in range(4):
                    nx = dx[d] + x
                    ny = dy[d] + y
                    
                    if 0<=nx<n and 0<=ny<m:
                        if object[nx][ny]==1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            
print(cnt)