# bronzeIII_15079
import sys
input = sys.stdin.readline
from math import sqrt

mapping = {
    'N':[0, 1], 'S':[0, -1],
    'E':[1, 0], 'W':[-1, 0],
    'NE':[sqrt(0.5), sqrt(0.5)],
    'SE':[sqrt(0.5), -sqrt(0.5)],
    'SW':[-sqrt(0.5), -sqrt(0.5)],
    'NW':[-sqrt(0.5), sqrt(0.5)]
}

n = int(input())
xy = list(map(float, input().split()))
for _ in range(n-1):
    dir, d = input().strip().split()
    d = float(d)
    
    move = mapping[dir]
    xy[0] += move[0]*d
    xy[1] += move[1]*d

print(f"{xy[0]:.8f} {xy[1]:.8f}")
