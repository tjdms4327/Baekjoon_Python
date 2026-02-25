import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
        
visited = [[False]*C for _ in range(R)]
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

count = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == '#' and not visited[r][c]:
            count += 1
            queue = deque()
            queue.append((r, c))
            visited[r][c] = True
            
            while queue:
                x, y = queue.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<R and 0<=ny<C:
                        if grid[nx][ny]=='#' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            
print(count)