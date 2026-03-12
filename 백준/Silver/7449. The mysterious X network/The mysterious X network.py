import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
    line = input().strip().split()
    c = int(line[0])
    nc = int(line[1])
    
    for x in line[2:]:
        x = int(x)
        graph[x].append(c)
        graph[c].append(x)
        

c1, c2 = map(int, input().split())
distance = [0]*n
queue = deque([c1])
visited = [False]*n
visited[c1] = True

while queue:
    cur = queue.popleft()
    
    if cur == c2:
        print(c1, c2, distance[cur]-1)
        break
    
    for next in graph[cur]:
        if not visited[next]:
            queue.append(next)
            visited[next] = True
            distance[next] = distance[cur] + 1