import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

MAX = 100001
visited = [False] * MAX

queue = deque()
queue.append((n, 0))
visited[n] = True
while queue:
    x, time = queue.popleft()
    if x == k:
        print(time)
        break
    
    for nx in (x-1, x+1, 2*x):
        if 0<=nx<MAX and not visited[nx]:
            visited[nx] = True
            queue.append((nx, time+1))