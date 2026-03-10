import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

'''
dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}
'''

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, n+1):
    graph[i].sort()
    
visited = [False] * (n+1)
order = [-1] * (n+1)

def dfs(r, depth):
    visited[r] = True
    order[r] = depth
    for x in graph[r]:
        if not visited[x]:
            dfs(x, depth+1)
            
dfs(r, 0)
for x in order[1:]:
    print(x)