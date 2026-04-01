import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    
    queue = deque([('1',1%n)])
    visited = [False]*n
    visited[1%n] = True
    
    while queue:
        s, mod = queue.popleft()
        if mod==0:
            print(s)
            break
        
        for digit in '01':
            new_s = s + digit
            new_mod = (mod*10 + int(digit))%n
            if not visited[new_mod]:
                visited[new_mod] = True
                queue.append((new_s, new_mod))