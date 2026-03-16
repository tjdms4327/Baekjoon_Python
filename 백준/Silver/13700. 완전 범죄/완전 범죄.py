import sys
input = sys.stdin.readline
from collections import deque

n, s, d, f, b, k = map(int, input().split())
I = list(map(int, input().split()))

queue = deque([(s, 0)])
visited = [False]*(n+1)
visited[s] = True

while queue:
    cur, button= queue.popleft()
    
    if cur == d:
        print(button)
        sys.exit()
    
    for nxt in [cur+f, cur-b]:
        if 0<nxt<=n and not visited[nxt] and nxt not in I:
            queue.append((nxt, button+1))
            visited[nxt] = True

print('BUG FOUND')