import sys
input = sys.stdin.readline
from collections import deque

d = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

n, m = map(int, input().split())
x, y = map(int, input().split())
x -= 1
y -= 1

queue = deque([(x, y, 0)])
visited = [[False]*n for _ in range(n)]
visited[x][y] = True


grid = [[-1]*n for _ in range(n)]
while queue:
    x, y, cnt = queue.popleft()
    grid[x][y] = cnt
    
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny]:
                queue.append((nx, ny, cnt+1))
                visited[nx][ny] = True

result = []
for _ in range(m):
    a, b = map(int, input().split())
    result.append(grid[a-1][b-1])
    
print(*result)