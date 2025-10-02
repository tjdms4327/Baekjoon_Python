import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

LOG = 17
parent = [[0] * (n+1) for _ in range(LOG)]
depth = [0] * (n+1)
visited = [False] * (n+1)

def dfs(node, d):
    visited[node] = True
    depth[node] = d
    for nxt in tree[node]:
        if not visited[nxt]:
            parent[0][nxt] = node
            dfs(nxt, d+1)
dfs(1, 0)

for k in range(1, LOG):
    for v in range(1, n+1):
        parent[k][v] = parent[k-1][parent[k-1][v]]

def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    for i in range(LOG):
        if diff & (1 << i):
            a = parent[i][a]

    if a == b:
        return a
    for i in reversed(range(LOG)):
        if parent[i][a] != parent[i][b]:
            a = parent[i][a]
            b = parent[i][b]
    return parent[0][a]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))