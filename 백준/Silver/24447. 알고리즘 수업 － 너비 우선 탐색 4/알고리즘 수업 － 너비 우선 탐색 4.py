import sys
input = sys.stdin.readline
from collections import deque

'''
bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    for each v ∈ V - {R}
        visited[v] <- NO;
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
    while (Q ≠ ∅) {
        u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
        for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
            if (visited[v] = NO) then {
                visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
                enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
            }
    }
}
'''

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for x in graph[1:]:
    x.sort()
    
queue = deque([r])
visited = [0]*(n+1)
visited[r] = 1
depth = [-1]*(n+1)
depth[r] = 0

cnt = 1
while queue:
    cur = queue.popleft()
    
    for x in graph[cur]:
        if not visited[x]:
            cnt += 1
            visited[x] = cnt
            depth[x] = depth[cur]+1
            queue.append(x)

tot = 0
for d, t in zip(visited, depth):
    tot += d*t
print(tot)