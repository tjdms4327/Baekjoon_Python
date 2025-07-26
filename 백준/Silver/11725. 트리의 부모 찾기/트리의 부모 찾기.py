import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7) # 재귀 제한 크게 설정

n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    u,v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 방향 없음

parent = [0] * (n + 1)
visited = [False] * (n + 1) # 중복 방문 방지
def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            dfs(v)

dfs(1)
for i in range(2, n + 1): # 1번은 루트임(부모 존재X)
    print(parent[i])
