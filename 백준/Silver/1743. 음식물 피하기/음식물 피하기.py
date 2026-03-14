import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())

trash = [[0]*(m+1) for _ in range(n+1)]
for _ in range(k):
    r, c = map(int, input().split())
    trash[r][c] = 1
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False]*(m+1) for _ in range(n+1)]
W = []

for r in range(1,1+n):
    for c in range(1, 1+m):
        if trash[r][c]==1 and not visited[r][c]:
            queue = deque([(r, c)])
            visited[r][c] = True
            w = 1
            
            while queue:
                x, y = queue.popleft()
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if 0<nx<=n and 0<ny<=m:
                        if not visited[nx][ny] and trash[nx][ny]==1:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            w += 1
            
            W.append(w)

print(max(W))