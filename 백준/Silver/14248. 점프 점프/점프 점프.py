import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
A = [0] + list(map(int, input().split()))

start = int(input())
queue = deque()
queue.append(start)
visited = [False] * (n+1)
visited[start] = True

while queue:
    cur = queue.popleft()
    
    for next in [cur-A[cur], cur+A[cur]]:
        if 0 < next <= n:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    
print(visited.count(True))