import sys
input = sys.stdin.readline
from collections import deque

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

queue = deque([(x1, y1)])
visited = [[False]*9 for _ in range(9)]
visited[x1][y1] = True

cnt = [[0]*9 for _ in range(9)]
while queue:
    x, y = queue.popleft()
    
    if (x, y) == (x2, y2):
        print(cnt[x][y])
        break
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 1<=nx<=8 and 1<=ny<=8:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt[nx][ny] = cnt[x][y] + 1
                