import sys 
input = sys.stdin.readline

from math import hypot

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]


distance = sum(
    hypot(x2 - x1, y2 - y1)
    for (x1, y1), (x2, y2) in zip(points, points[1:]+ [points[0]])
)
print(int(distance))