# silverII_18352
import sys
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split())
A = [[] for _ in range(n+1)]
answer = []
visited = [-1] * (n+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if visited[i] == -1:
                visited[i] = visited[now_node] + 1
                queue.append(i)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    
BFS(x)
for i in range(n+1):
    if visited[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)