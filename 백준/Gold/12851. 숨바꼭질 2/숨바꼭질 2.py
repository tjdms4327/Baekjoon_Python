import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

queue = deque([n])
dist = [-1]*100001
dist[n] = 0
count = [0]*100001
count[n] = 1

while queue:
    cur = queue.popleft()

    for nx in (cur-1, cur+1, cur*2):
        if 0 <= nx <= 100000:
            if dist[nx] == -1:
                dist[nx] = dist[cur] + 1
                count[nx] = count[cur]
                queue.append(nx)
            elif dist[nx] == dist[cur] + 1:
                count[nx] += count[cur]

print(dist[k])
print(count[k])