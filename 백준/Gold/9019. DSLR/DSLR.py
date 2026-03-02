import sys
input = sys.stdin.readline
from collections import deque
def D(n):
    return (2*n) % 10000
def S(n):
    return ((10000+n)-1) % 10000
def L(n):
    return (n % 1000) * 10 + (n // 1000)
def R(n):
    return (n % 10) * 1000 + (n // 10)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    queue = deque()
    queue.append(a)
    visited = [False] * 10000
    visited[a] = True
    
    parent = [-1] * 10000
    how = [''] * 10000
    
    while queue:
        cur = queue.popleft()
        if cur == b:
            break
        
        for nx, cmd in [(D(cur), 'D'), (S(cur), 'S'), (L(cur), 'L'), (R(cur), 'R')]:
            if not visited[nx]:
                visited[nx] = True
                queue.append(nx)
                parent[nx] = cur
                how[nx] = cmd
    
    result = ''
    cur = b
    while cur != a:
        result += how[cur]
        cur = parent[cur]
        
    print(result[::-1])