# silverI_1325
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
answer = [0] * (n+1)

def BFS(v):
    visited = [False] * (n+1)
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                queue.append(i)
   
for i in range(m):
    s, e = map(int, input().split())
    A[s].append(e)

for i in range(1, n+1):
    BFS(i)
maxVal = max(answer)
for i in range(1, n+1):
    if maxVal == answer[i]:
        print(i, end=' ')