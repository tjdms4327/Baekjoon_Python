import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    
    MAP = [list(map(int, input().split())) for _ in range(h)]
    
    count = 0
    visited = [[False]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if MAP[r][c] == 1 and not visited[r][c]:
                queue = deque()
                queue.append((r, c))
                visited[r][c] = True
                
                while queue:
                    x, y = queue.popleft()
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        
                        if 0<=nx<h and 0<=ny<w:
                            if MAP[nx][ny]==1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
            
                count += 1
            
    print(count)