import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    line = list(map(int, input().strip().split()))
    n = line[0]
    k = line[1]
    
    if n == 0:
        print('Connected.')
        continue
    elif n > 1 and k == 0:
        print('Not connected.')
        continue
    
    graph = [[] for _ in range(n)]
    for i in range(2, 2*k+2, 2):
        x, y = line[i], line[i+1]
        graph[x].append(y)
        graph[y].append(x)
        
    
    
    visited = [False]*n
    visited[0] = True
    queue = deque()
    queue.append(0)
    while queue:
        cur = queue.popleft()
        
        for next in graph[cur]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                
        
    if visited.count(True) == n:
        print('Connected.')
    else:
        print('Not connected.')