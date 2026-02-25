import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())

tomato = []
queue = deque()
for h in range(H):
    box = []
    for n in range(N):
        row = list(map(int, input().split()))
        box.append(row)
        
        for m in range(M):
            if row[m] == 1:
                queue.append((h,n,m))
    tomato.append(box)


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
   
while queue:
    z, x, y = queue.popleft()

    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
            if tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                queue.append((nz, nx, ny))
                
max_day = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 0:
                print(-1)
                sys.exit()
            max_day = max(max_day, tomato[h][n][m])
            
print(max_day - 1)