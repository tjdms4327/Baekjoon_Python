import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a, c))
    
queue = deque([(1, 0)])
visited = [False] * (n+1)
visited[1] = True
distance = [0] * (n+1)

while queue:
    cur, d = queue.popleft()
    
    for next, nd in graph[cur]:
        if not visited[next]:
            distance[next] = d + nd
            queue.append((next, d+nd))
            visited[next] = True
            
print(max(distance))