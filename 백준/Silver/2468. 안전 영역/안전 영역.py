import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
ground = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = -1
for rain in range(0, max(map(max, ground))+1):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c] and ground[r][c]>rain:
                queue = deque([(r, c)])
                visited[r][c] = True
                
                while queue:
                    x, y = queue.popleft()
                    
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        
                        if 0<=nx<n and 0<=ny<n:
                            if not visited[nx][ny] and ground[nx][ny]>rain:
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                
                cnt += 1
                        
    ans = max(ans, cnt)
    
    
print(ans)
                        