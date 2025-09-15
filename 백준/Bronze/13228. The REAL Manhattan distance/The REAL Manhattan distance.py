import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, floor1, x2, y2, floor2 = map(int, input().split())
    distance = floor1 + abs(x1 - x2) + abs(y1 - y2) + floor2
    print(distance)