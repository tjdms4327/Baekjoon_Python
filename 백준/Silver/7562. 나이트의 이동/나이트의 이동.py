import sys
input = sys.stdin.readline
from collections import deque    
        
dx = [1, 1, -1, -1, 2, -2, 2, -2]
dy = [2, -2, 2, -2, 1, 1, -1, -1]

t = int(input())
for _ in range(t):
    I = int(input())
    x, y = tuple(map(int, input().split()))
    target = tuple(map(int, input().split()))
    
    queue = deque([(x, y, 0)])
    visited = [[False]*I for _ in range(I)]
    visited[x][y] = True
    
    while queue:
        x, y, d = queue.popleft()
        
        if (x, y) == target:
            print(d)
            break
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<I and 0<=ny<I:
                if not visited[nx][ny]:
                    queue.append((nx, ny, d+1))
                    visited[nx][ny] = True