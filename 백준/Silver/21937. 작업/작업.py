import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    
x = int(input())
queue = deque([x])
visited = [False]*(n+1)
visited[x] = True

cnt = 0
while queue:
    cur = queue.popleft()
    
    for prev in graph[cur]:
        if not visited[prev]:
            visited[prev] = True
            queue.append(prev)
            cnt += 1
            
print(cnt)