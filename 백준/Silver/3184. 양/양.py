import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
yard = [list(input().strip()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

total_sheep, total_wolf = 0, 0

visited = [[False]*c for _ in range(r)]
for x in range(r):
    for y in range(c):
        if not visited[x][y] and yard[x][y]!='#':
            queue = deque([(x, y)])
            visited[x][y] = True
            
            sheep = 0
            wolf = 0
            
            while queue:
                cx, cy = queue.popleft()    
                if yard[cx][cy] == 'o':
                    sheep += 1
                elif yard[cx][cy] == 'v':
                    wolf += 1
                    
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    
                    if 0 <= nx < r and 0 <= ny < c:
                        if not visited[nx][ny] and yard[nx][ny] != '#':
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf
                
                
print(total_sheep, total_wolf)