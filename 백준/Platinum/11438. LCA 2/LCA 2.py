# platinumV_11438
import sys
from collections import deque
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0] * (n+1)
visited = [False] * (n+1)

LOG = 1
while (1 << LOG) <= n:
    LOG += 1

parent = [[0] * (n+1) for _ in range(LOG)]

def bfs(root):
    q = deque([root])
    visited[root] = True
    depth[root] = 0
    while q:
        now = q.popleft()
        for nxt in tree[now]:
            if not visited[nxt]:
                visited[nxt] = True
                parent[0][nxt] = now
                depth[nxt] = depth[now] + 1
                q.append(nxt)
bfs(1)

for k in range(1, LOG):
    for v in range(1, n+1):
        parent[k][v] = parent[k-1][parent[k-1][v]]

def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    for k in range(LOG-1, -1, -1):
        if diff & (1 << k):
            a = parent[k][a]
    if a == b:
        return a
    for k in range(LOG-1, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
    return parent[0][a]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    write(str(lca(a, b)) + '\n')