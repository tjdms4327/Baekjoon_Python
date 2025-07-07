import sys
input=sys.stdin.readline

import math

h, w=map(int, input().split())
area=h*w/4840.0
print(math.ceil(area/5))