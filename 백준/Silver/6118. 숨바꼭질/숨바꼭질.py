import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

barn = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    barn[a].append(b)
    barn[b].append(a)
    
    
queue = deque([(1, 0)])
visited = [False] * (n+1)
visited[1] = True
dist = {}

while queue:
    cur, d = queue.popleft()
    if d in dist:
        dist[d].append(cur)
    else:
        dist[d] = [cur]
    
    for nxt in barn[cur]:
        if not visited[nxt]:
            queue.append((nxt, d+1))
            visited[nxt] = True
            
MAX = max(dist.keys())
hide = sorted(dist[MAX])

print(hide[0], MAX, len(hide))