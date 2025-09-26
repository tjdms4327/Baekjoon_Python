# platinumV_1219
import sys
input = sys.stdin.readline

n, scity, ecity, m = map(int, input().split())
edges = []
distance = [-sys.maxsize] * n # 최단거리 리스트 초기화

for _ in range(m):
    start, end, price = map(int, input().split())
    edges.append((start, end, price))

citymoney = list(map(int, input().split()))

# 변형된 벨만-포드
distance[scity] = citymoney[scity] # 출발 초기화
for i in range(n+101):
    for start, end, price in edges:
        if distance[start] == -sys.maxsize:
            continue
        elif distance[start] == sys.maxsize:
            distance[end] = sys.maxsize
        elif distance[end] < distance[start] + citymoney[end] - price:
            distance[end] = distance[start] + citymoney[end] - price
            if i >= n-1:
                distance[end] = sys.maxsize

if distance[ecity] == -sys.maxsize:
    print('gg')
elif distance[ecity] == sys.maxsize:
    print('Gee')
else:
    print(distance[ecity])