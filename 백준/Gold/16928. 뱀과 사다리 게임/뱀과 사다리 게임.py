import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

board = {}
for _ in range(n+m):
    x, y = map(int, input().split())
    board[x] = y

start = 1
visited = [False] * 101    
visited[start] = True
q = deque()
q.append((1, 0))

while q:
    cur, dist = q.popleft()
    if cur == 100:
        print(dist)
        break
    
    for dice in range(1, 7):
        next_pos = cur + dice
        if next_pos > 100:
            continue
        
        if next_pos in board:
            next_pos = board[next_pos]
        if not visited[next_pos]:
            visited[next_pos] = True
            q.append((next_pos, dist+1))
