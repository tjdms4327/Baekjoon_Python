import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())

change = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    change[x].append(y)
    change[y].append(x)
    
queue = deque()
queue.append(a)
visited = [False] * (n+1)
visited[a] = True

dist = [0] * (n+1)
while queue:
    cur = queue.popleft()
    
    if cur == b:
        print(dist[cur])
        sys.exit()
        
    for next in change[cur]:
        if not visited[next]:
            visited[next] = True
            queue.append(next)
            dist[next] = dist[cur] + 1

print(-1)