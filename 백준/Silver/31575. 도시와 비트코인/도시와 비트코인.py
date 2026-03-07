import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(m)]

if m==1 and n==1:
    print('Yes')
    sys.exit()
    
    

dx = [1, 0]
dy = [0, 1]

start = (0,0)
queue = deque()
queue.append(start)
visited = [[False]*n for _ in range(m)]
visited[start[0]][start[1]] = True

while queue:
    r, c = queue.popleft()
    for i in range(2):
        row = r + dx[i]
        col = c + dy[i]
        
        if 0<=row<m and 0<=col<n and map[row][col]==1 and not visited[row][col]:
            queue.append((row, col))
            visited[row][col] = True
            
            if row==m-1 and col==n-1:
                print('Yes')
                sys.exit()
                
print('No')