import sys
input=sys.stdin.readline

import math

d,h,w=map(int, input().split())
n=math.sqrt(d**2/(h**2+w**2))
print(int(n*h), int(n*w))