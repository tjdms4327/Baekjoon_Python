import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

t = int(input())
for case in range(t):
    h, w = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    
    cnt = 0
    visited = [[False]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c]=='#' and not visited[r][c]:
                queue = deque([(r, c)])
                visited[r][c] = True
                cnt += 1
                
                while queue:
                    x, y = queue.popleft()
                    
                    for i in range(4):
                        nx = dx[i] + x
                        ny = dy[i] + y
                        
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]=='#' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
    
    print(cnt)