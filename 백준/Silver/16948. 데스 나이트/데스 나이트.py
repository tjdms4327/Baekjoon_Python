import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

move = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

queue = deque([(r1, c1, 0)])
visited = [[False]*(n) for _ in range(n)]
visited[r1][c1] = True

while queue:
    x, y, cnt = queue.popleft()
    
    if (x, y) == (r2, c2):
        print(cnt)
        sys.exit()
        
    for dx, dy in move:
        nx = dx+x
        ny = dy+y
        
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny]:
                queue.append((nx, ny, cnt+1))
                visited[nx][ny] = True
                
print(-1)