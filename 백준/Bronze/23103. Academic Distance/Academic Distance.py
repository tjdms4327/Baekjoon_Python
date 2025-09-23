# bronzeIII_22103.py
import sys
input = sys.stdin.readline

n = int(input())
coordinates = [tuple(map(int, input().split()))for _ in range(n)]

distance = 0
for i in range(1, n):
    distance += abs(coordinates[i][0] - coordinates[i-1][0]) + abs(coordinates[i][1] - coordinates[i-1][1])
print(distance)