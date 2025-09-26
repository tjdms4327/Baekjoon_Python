# silverI_11403
n = int(input())
distance = [[0 for j in range(n)] for i in range(n)]

# 인접 행렬 데이터
for i in range(n):
    distance[i] = list(map(int, input().split()))
    
# 변형된 플로이드-워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if distance[i][k] == 1 and distance[k][j] == 1:
                distance[i][j] = 1

for i in range(n):
    for j in range(n):
        print(distance[i][j], end=' ')
    print()