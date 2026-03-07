import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
start, end = map(int, input().split())

m = int(input())
relationships = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    relationships[x].append(y)
    relationships[y].append(x)
        

queue = deque()
queue.append(start)
visited = [False]*(n+1)
visited[start] = True

dist = [0] * (n+1)
while queue:
    cur = queue.popleft()
    
    if cur == end:
        print(dist[cur])
        sys.exit()
        
    for x in relationships[cur]:
        if not visited[x]:
            visited[x] = True
            queue.append(x)
            dist[x] = dist[cur] + 1

print(-1)