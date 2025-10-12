# bronzeII_11113
import sys
input = sys.stdin.readline

n = int(input())
xy = [(tuple(map(float, input().split()))) for _ in range(n)]

m = int(input())
for _ in range(m):
    p = int(input())
    order = list(map(int, input().split()))
    
    distance = 0
    for i in range(1, p):
        x0, y0 = xy[order[i-1]]
        x1, y1 = xy[order[i]]
        distance += ((x1-x0)**2 + (y1-y0)**2)**0.5
    print(round(distance))