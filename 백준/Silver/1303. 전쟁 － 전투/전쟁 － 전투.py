import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(m)]

visited = [[False]*n for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

white, blue = 0,0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            q = deque([(i,j)])
            visited[i][j] = True
            color = board[i][j]
            cnt = 1
            
            while q:
                x,y = q.popleft()
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    
                    if 0<=nx<m and 0<=ny<n:
                        if not visited[nx][ny] and board[nx][ny]==color:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                            cnt+=1
            
            if color=='W':
                white += cnt*cnt
            else:
                blue += cnt*cnt

print(white, blue)