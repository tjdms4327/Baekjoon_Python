import sys
input = sys.stdin.readline
from collections import deque

n, m, start = map(int, input().split())
A = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)
for i in range(n + 1):
    A[i].sort()
    
def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
visited = [False] * (n + 1)
DFS(start)
print()

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        print(now_node, end=' ')
        for i in A[now_node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
visited = [False] * (n + 1)
BFS(start)