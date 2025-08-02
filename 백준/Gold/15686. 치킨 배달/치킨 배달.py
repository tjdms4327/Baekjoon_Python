import sys
input=sys.stdin.readline

from itertools import combinations

n, m=map(int, input().strip().split())
matrix=[list(map(int, input().strip().split())) for _ in range(n)]

house=[]
chicken=[]

for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            house.append((i, j))
        elif matrix[i][j]==2:
            chicken.append((i, j))



min_tot_distance=float('inf')
for selected_chicken in combinations(chicken, m):
    tot_distance=0
    for x, y in house:
        distance=min(abs(x-cx)+abs(y-cy) for cx, cy in selected_chicken)
        tot_distance+=distance
    min_tot_distance=min(min_tot_distance, tot_distance)
print(min_tot_distance)