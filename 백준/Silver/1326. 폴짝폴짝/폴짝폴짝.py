import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())
a -= 1; b -= 1

if a == b:
    print(0)
    sys.exit()

start = a
queue = deque()
queue.append(start)
visited = [False]*n
visited[start] = True

jump = [0]*n
while queue:
    cur = queue.popleft()
    
    if cur == b:
        print(jump[cur])
        sys.exit()
        
    x = cur
    dist = bridge[cur]
    while x+dist < n:
        x += dist
        if not visited[x]:
            jump[x] = jump[cur] + 1
            queue.append(x)
            visited[x] = True
    x = cur
    while x - dist >= 0:
        x -= dist
        if not visited[x]:
            jump[x] = jump[cur] + 1
            visited[x] = True
            queue.append(x)

print(-1)