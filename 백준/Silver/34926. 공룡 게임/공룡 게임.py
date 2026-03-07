import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
map = list(input().strip())

if n == 1:
    print('YES')
    sys.exit()
    
    
    
d = [1, k]

start = 0
queue = deque()
queue.append(start)
visited = [False]*n
visited[start] = True

while queue:
    cur = queue.popleft()
    
    for i in d:
        next = cur + i
        if next < n and map[next]!='#' and not visited[next]:
            queue.append(next)
            visited[next] = True
            
            if next == n-1:
                print('YES')
                sys.exit()
                
print('NO')