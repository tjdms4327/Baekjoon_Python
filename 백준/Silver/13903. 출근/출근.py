import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

n = int(input())
D = set()
for _ in range(n):
    x, y = map(int, input().split())
    D.add((x, y))

queue = deque()
visited = [[False]*c for _ in range(r)]
for j in range(c):
    if grid[0][j] == 1:
        queue.append((0, j, 0))
        visited[0][j] = True

while queue:
    x, y, d = queue.popleft()
    
    if x == r-1:
        print(d)
        sys.exit()
        
    for dx, dy in D:
        nx = x + dx
        ny = y + dy
        
        if 0<=nx<r and 0<=ny<c:
            if not visited[nx][ny] and grid[nx][ny]==1:
                queue.append((nx, ny, d+1))
                visited[nx][ny] = True
                
print(-1)