# silverV_24775
import sys
input = sys.stdin.readline
from math import cos, sin, radians

n = int(input())
for _ in range(n):
    v0, angle, x, h1, h2 = map(float, input().split())
    angle = radians(angle)
    
    t = x / (v0 * cos(angle))
    y = v0 * t * sin(angle) - 0.5 * 9.81 * (t**2)
    
    if h1 + 1 <= y <= h2 - 1:
        print('Safe')
    else:
        print('Not Safe')