import sys
sys.setrecursionlimit(10000) # 재귀 호출 최대 깊이
input = sys.stdin.readline
n, m = map(int, input().split()) # 노드 수, 에지 수
arrive = False
A = [[] for _ in range(n+1)] # 그래프 데이터 저장 인접 리스트
visited = [False] * (n+1) # 방문 기록 저장 리스트

def DFS(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth + 1) # 재귀 호출마다 깊이 증가
    visited[now] = False

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(n):
    DFS(i, 1)
    if arrive: break
if arrive:
    print(1)
else:
    print(0)