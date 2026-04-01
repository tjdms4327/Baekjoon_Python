import sys
input = sys.stdin.readline
from collections import deque

d = [(1,0),(-1,0),(0,1),(0,-1)]

t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    maze = []
    for i in range(r):
        line = list(input().strip())
        maze.append(line)
        if 'S' in line:
            sr, sc = i, line.index('S')

    visited = [[False]*c for _ in range(r)]
    queue = deque([(sr, sc, 0)])
    visited[sr][sc] = True

    found = False
    while queue:
        x, y, dist = queue.popleft()
        if maze[x][y] == 'G':
            print(f"Shortest Path: {dist}")
            found = True
            break
        
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and maze[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist+1))
                    
    if not found:
        print("No Exit")