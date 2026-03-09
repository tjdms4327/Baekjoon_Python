import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
connected = [[] for _ in range(n+1)]
for _ in range(m):
    c1, c2 = map(int, input().split())
    connected[c1].append(c2)
    connected[c2].append(c1)
    
    
queue = deque()
queue.append(1)
visited = [False] * (n+1)
visited[1] = True

while queue:
    cur = queue.popleft()
    
    for next in connected[cur]:
        if not visited[next]:
            queue.append(next)
            visited[next] = True
            
ok = False
for idx, tf in enumerate(visited[1:], start=1):
    if not tf:
        print(idx)
        ok = True
        
if not ok:
    print(0)