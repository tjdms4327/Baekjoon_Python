# bronzeIV_34529
import sys
input = sys.stdin.readline
from math import ceil

x, y, z = map(int, input().split())
u, v, w = map(int, input().split())
print(x*ceil(u/100) + y*ceil(v/50)+ z*ceil(w/20))