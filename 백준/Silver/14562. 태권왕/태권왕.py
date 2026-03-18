import sys
input = sys.stdin.readline
from collections import deque

c = int(input())
for _ in range(c):
    s, t = map(int, input().split())
    
    queue = deque([(s, t, 0)])
    visited = set()
    visited.add((s, t))
    while queue:
        s, t, cnt = queue.popleft()
        
        if s == t:
            print(cnt)
            break
    
        ns, nt = 2*s, t+3
        if ns <= nt and (ns, nt) not in visited:
            visited.add((ns, nt))
            queue.append((ns, nt, cnt+1))
        
        ns, nt = s+1, t
        if ns <= nt and (ns, nt) not in visited:
            visited.add((ns, nt))
            queue.append((ns, nt, cnt+1))