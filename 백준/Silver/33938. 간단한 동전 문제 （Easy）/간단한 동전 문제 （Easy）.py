import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
if n == 0:
    if m == 0:
        print(0)
    else:
        print(-1)
    sys.exit()

P = list(map(int, input().split()))
if n == 1:
    p = P[0]
    if p == 0:
        if m == 0:
            print(0)
        else:
            print(-1)
    else:
        if m % p == 0:
            k = m // p
            if k >= 0:
                print(k)
            else:
                print(-1)
        else:
            print(-1)

elif n == 2:
    queue = deque([0])
    visited = set([0])
    dist = {0: 0}

    LIMIT = 2000  
    while queue:
        cur = queue.popleft()
        if cur == m:
            print(dist[cur])
            break
        for coin in P:
            nxt = cur + coin
            if -LIMIT <= nxt <= LIMIT and nxt not in visited:
                visited.add(nxt)
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)
    else:
        print(-1)