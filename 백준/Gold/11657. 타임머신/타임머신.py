# goldIV_1657
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
distance = [sys.maxsize] * (n+1)

for i in range(m):
    s, e, time = map(int, input().split())
    edges.append((s, e, time))
    
# 벨만-포드 수행
distance[1] = 0
for _ in range(n-1):
    for s, e, time in edges:
        if distance[s] != sys.maxsize and distance[e] > distance[s] + time:
            distance[e] = distance[s] + time
# 음수 사이클 확인
myCycle = False
for s, e, time in edges:
        if distance[s] != sys.maxsize and distance[e] > distance[s] + time:
            myCycle = True

if not myCycle:
    for i in range(2, n+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)