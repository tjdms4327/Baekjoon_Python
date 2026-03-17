import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n+1)
queue = deque([1])
dist[1] = 0

# 초기 BFS (1번 도시 기준)
while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            queue.append(nxt)


q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    queue = deque()
    # 갱신 시작점
    if dist[a] != -1 and (dist[b] == -1 or dist[b] > dist[a] + 1):
        dist[b] = dist[a] + 1
        queue.append(b)
    if dist[b] != -1 and (dist[a] == -1 or dist[a] > dist[b] + 1):
        dist[a] = dist[b] + 1
        queue.append(a)
    
    # 감소 전파
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1 or dist[nxt] > dist[cur] + 1:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)
    
    print(*dist[1:])