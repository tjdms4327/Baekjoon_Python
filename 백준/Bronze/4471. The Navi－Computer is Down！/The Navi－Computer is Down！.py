# bronzeII_4471
import sys
input = sys.stdin.readline
from math import sqrt

n = int(input())
for _ in range(n):
    now = input().strip()
    x1, y1, z1 = map(float, input().split())
    dest = input().strip()
    x2, y2, z2 = map(float, input().split())
    
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f'{now} to {dest}: {distance:.2f}')