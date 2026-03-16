import sys
input = sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int, input().split())
button = [u, -d]

queue = deque([(s, 0)])
visited = [False]*(f+1)
visited[s] = True
dist = [0] * (f+1)

while queue:
    cur, d = queue.popleft()
    
    if cur == g:
        print(d)
        sys.exit()
    
    for b in button:
        next = cur + b
        
        if 0<next<=f and not visited[next]:
            queue.append((next, d+1))
            visited[next] = True
            

print('use the stairs')