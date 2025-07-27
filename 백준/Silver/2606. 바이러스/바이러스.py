import sys
input=sys.stdin.readline

n=int(input()) # 컴퓨터 수
m=int(input()) # 연결 수
graph=[[] for i in range(n+1)]
for _ in range(m):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(n+1)
virus=0
def dfs(start):
    global virus
    visited[start]=True
    for next in graph[start]:
        if not visited[next]:
            virus+=1
            dfs(next)
dfs(1)
print(virus)