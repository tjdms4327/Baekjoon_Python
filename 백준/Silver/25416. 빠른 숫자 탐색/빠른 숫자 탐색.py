import sys
input = sys.stdin.readline
from collections import deque

board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque([(r, c, 0)])
visited = [[False]*5 for _ in range(5)]
visited[r][c] = True
for i in range(5):
    for j in range(5):
        if board[i][j] == -1:
            visited[i][j] = True
            
while queue:
    x, y, cnt = queue.popleft()
    
    if board[x][y] == 1:
        print(cnt)
        sys.exit()
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if 0<=nx<5 and 0<=ny<5:
            if not visited[nx][ny]:
                queue.append((nx, ny, cnt+1))
                visited[nx][ny] = True
                
print(-1)