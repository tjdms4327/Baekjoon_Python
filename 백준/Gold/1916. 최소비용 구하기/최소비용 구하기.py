import sys
input=sys.stdin.readline

import heapq

n=int(input()) # 도시 
m=int(input()) # 버스 수
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u, v, w= map(int, input().split()) # 출발도시, 도착 도시, 버스비
    graph[u].append((v, w))
start, end=map(int, input().split()) # 출발지, 도착지



INF=int(1e9)
dist=[INF]*(n+1)

def dijkstra(start):
    q = [] # 우선순위 
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, now = heapq.heappop(q) # 비용 가장 작은 거 꺼냄 # now는 방문할 도시 번호
        if dist[now] < cost: # 더 좋은 비용으로 이 도시 방문한 적 있으면
            continue
        if now == end:
            break

        for nxt, w in graph[now]: # 현재 도시와 인접한 도시와 비 순회
            nd = cost + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(q, (nd, nxt))

dijkstra(start)
print(dist[end])