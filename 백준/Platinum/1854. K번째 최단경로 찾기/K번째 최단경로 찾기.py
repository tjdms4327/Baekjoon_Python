# platinumIv_1854
import sys
input = sys.stdin.readline
import heapq

n, m, k = map(int, input().split())
W = [[] for _ in range(n+1)]
distance = [[sys.maxsize] * k for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    W[a].append((b, c))
    
pq = [(0, 1)] # (가중치, 목표 노드)
distance[1][0] = 0

while pq: # 변형된 다익스트라 
    cost, node = heapq.heappop(pq)
    for nNode, nCost in W[node]:
        sCost = cost + nCost # 새 거리 = 현재 노드의 거리 + 에지 가중치
        if distance[nNode][k-1] > sCost:
            distance[nNode][k-1] = sCost
            distance[nNode].sort()
            heapq.heappush(pq, [sCost, nNode])
        
for i in range(1, n+1):
    if distance[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][k-1])