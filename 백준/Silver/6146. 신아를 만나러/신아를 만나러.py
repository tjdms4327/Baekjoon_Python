import sys
input = sys.stdin.readline
from collections import deque

x, y, n = map(int, input().split())

SHIFT = 500
SIZE = 1001
rain = [[False]*SIZE for _ in range(SIZE)]
for _ in range(n):
    a, b = map(int, input().split())
    rain[a+SHIFT][b+SHIFT] = True
    
sx, sy = SHIFT, SHIFT
tx, ty = x+SHIFT, y+SHIFT    
queue = deque([(sx, sy, 0)])
visited = [[False]*SIZE for _ in range(SIZE)]
visited[sx][sy] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y, d = queue.popleft()

    if x == tx and y == ty:
        print(d)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < SIZE and 0 <= ny < SIZE:
            if not visited[nx][ny] and not rain[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, d+1))