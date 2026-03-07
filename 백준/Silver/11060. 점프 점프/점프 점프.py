import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
A = list(map(int, input().split()))

if n == 1:
    print(0)
    sys.exit()

start = 0
queue = deque()
queue.append(start)
visited = [False] * n
visited[start] = True

count = [0]*n
while queue:
    cur = queue.popleft()

    if cur == n-1:
        print(count[cur])
        sys.exit()
        
    for x in range(cur+1, cur+A[cur]+1):
        if x<n and not visited[x]:
            count[x] = count[cur] + 1
            visited[x] = True
            queue.append(x)
    
print(-1)