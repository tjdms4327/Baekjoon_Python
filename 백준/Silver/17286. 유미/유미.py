# silverV_17286
import sys
input = sys.stdin.readline

cat_xy = list(map(int, input().split()))
xy = [tuple(map(int, input().split())) for _ in range(3)]

distance12 = ((xy[0][0] - xy[1][0])**2 + (xy[0][1] - xy[1][1])**2)**0.5
distance23 = ((xy[2][0] - xy[1][0])**2 + (xy[2][1] - xy[1][1])**2)**0.5
distance13 = ((xy[0][0] - xy[2][0])**2 + (xy[0][1] - xy[2][1])**2)**0.5

cat_distance = [((xy[i][0] - cat_xy[0])**2 + (xy[i][1] - cat_xy[1])**2)**0.5 for i in range(3)]
cand = [cat_distance[0] + distance23 + min(distance12, distance13),
        cat_distance[1]+ distance13 + min(distance12, distance23),
        cat_distance[2] + distance12 + min(distance13, distance23)]
print(int(min(cand)))