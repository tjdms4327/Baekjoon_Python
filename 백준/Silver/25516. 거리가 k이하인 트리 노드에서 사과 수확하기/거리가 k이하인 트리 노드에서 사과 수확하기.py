import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
children = [[] for _ in range(n)]
for _ in range(n-1):
    p, c = map(int, input().split())
    children[p].append(c)
    
apples = list(map(int, input().split()))

queue = deque([(0,0)]) #(cur, k)
visited = [False]*n
cnt = 0
while queue:
    cur, i = queue.popleft()
    if i <= k:
        cnt += apples[cur]
    else:
        break
    
    for next in children[cur]:
        if not visited[next]:
            visited[next] = True
            queue.append((next, i+1))

print(cnt)