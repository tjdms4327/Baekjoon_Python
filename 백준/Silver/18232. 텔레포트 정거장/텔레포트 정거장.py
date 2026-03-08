import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
s, e = map(int, input().split())

move = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    move[x].append(y)
    move[y].append(x)
    
    
queue = deque()
queue.append(s)
visited = [False]*(n+1)
visited[s] = True

time = [0]*(n+1)
while queue:
    cur = queue.popleft()
    
    if cur == e:
        print(time[cur])
        sys.exit()
        
    for next in move[cur] + [cur-1, cur+1]:
        if 0<next<=n:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                time[next] = time[cur] + 1
                