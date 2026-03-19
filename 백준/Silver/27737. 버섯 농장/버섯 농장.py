import sys
input = sys.stdin.readline
from collections import deque

d = [(1,0),(-1,0),(0,1),(0,-1)]

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]
need = 0

for r in range(n):
    for c in range(n):
        if grid[r][c] == 0 and not visited[r][c]:
            queue = deque([(r, c)])
            visited[r][c] = True
            size = 1
            
            while queue:
                x, y = queue.popleft()
                
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy
                    
                    if 0 <= nx < n and 0 <= ny < n:
                        if not visited[nx][ny] and grid[nx][ny] == 0:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                            size += 1
            
            need += (size + k - 1) // k

if need == 0 or need > m:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(m - need)