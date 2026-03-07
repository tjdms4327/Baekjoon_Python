import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())

friends = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
    
start = 1
queue = deque()
queue.append(start)
visited = [False]*(n+1)
visited[start] = True

dist = [0] * (n+1)
while queue:
    cur = queue.popleft()
    
    for x in friends[cur]:
        if not visited[x]:
            visited[x] = True
            queue.append(x)
            dist[x] = dist[cur] + 1

            
count = 0
for i in range(2, n+1):
    if 0 < dist[i] <= 2:
        count += 1
print(count)