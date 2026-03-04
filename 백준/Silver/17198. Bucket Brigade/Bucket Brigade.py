import sys
input = sys.stdin.readline
from collections import deque

matrix = [list(input().strip()) for _ in range(10)]

for r in range(10):
    for c in range(10):
        if matrix[r][c] == 'B':
            fire = (r, c)
        elif matrix[r][c] == 'L':
            lake = (r, c, 0)



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[False]*10 for _ in range(10)]
visited[lake[0]][lake[1]] = True

queue = deque()
queue.append(lake)
while queue:
    row, col, distance = queue.popleft()
    for i in range(4):
        r = row + dr[i]
        c = col + dc[i]
        
        if 0<=r<10 and 0<=c<10:
            if matrix[r][c] != 'R' and not visited[r][c]:
                queue.append((r, c, distance+1))
                visited[r][c] = True
            
    if matrix[row][col] == 'B':
        print(distance-1)
        break