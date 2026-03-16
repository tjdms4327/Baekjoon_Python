import sys
input = sys.stdin.readline
from collections import deque

a, b, n, m = map(int, input().split())

move = [1, -1, a, -a, b, -b, 'mult_a', 'mult_b']

queue = deque([(n, 0)])
visited = [False]*100001
visited[n] = True

while queue:
    cur, cnt = queue.popleft()
    
    if cur == m:
        print(cnt)
        break
    
    for x in move:
        if x == 'mult_a':
            nxt = cur*a
        elif x == 'mult_b':
            nxt = cur*b
        else:
            nxt = cur + x
            
        if 0<=nxt<100001 and not visited[nxt]:
            visited[nxt] = True
            queue.append((nxt, cnt+1))