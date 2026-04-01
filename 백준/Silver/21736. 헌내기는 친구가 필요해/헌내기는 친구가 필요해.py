import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())

campus = []
for i in range(n):
    line = list(input().strip())
    campus.append(line)
    
    if 'I' in line:
        c = line.index('I')
        start = (i, c)

        
visited = [[False]*m for _ in range(n)]
queue = deque()
queue.append(start)
visited[start[0]][start[1]] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and campus[nx][ny] != 'X':
                visited[nx][ny] = True
                queue.append((nx, ny))
                
                if campus[nx][ny] == 'P':
                    count += 1
                    
if count == 0:
    print('TT')
else:
    print(count)