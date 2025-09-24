# goldIV_1753
import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, e = map(int, input().split())
k = int(input()) # 출발 노드
distance = [sys.maxsize] * (V+1)
visited = [False] * (V+1)
myList = [[] for _ in range(V+1)]
q = PriorityQueue()

for _ in range(e):
    u, v, w = map(int, input().split())
    myList[u].append((v, w))

q.put((0, k)) # 시작점 설정
distance[k] = 0

while q.qsize() > 0:
    current = q.get()
    c_v = current[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for tmp in myList[c_v]:
        next = tmp[0]
        val = tmp[1]
        if distance[next] > distance[c_v] + val: # 최소 거리 업데이트
            distance[next] = distance[c_v] + val
            q.put((distance[next], next))
    
for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print('INF')