
n,m,v=map(int, input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for adj in graph:
    adj.sort()

# DFS - 재귀 사용
visited=[False]*(n+1)
def dfs(v, visited):
    visited[v]=True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited)

# BFS - 큐 사용
from collections import deque
def bfs(start):
    visited=[False]*(n+1)
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor]=True
                queue.append(neighbor)

dfs(v, visited) ; print()
bfs(v)