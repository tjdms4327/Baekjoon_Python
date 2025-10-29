# silverIV_11558
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    lst = [0]*(n+1)
    for i in range(1, n+1):
        lst[i] = int(input())
    
    count = 0
    cur = 1
    visited = set()
    while cur != n:
        if cur in visited:
            count = 0
            break
        visited.add(cur)
        cur = lst[cur]
        count += 1
    print(count)