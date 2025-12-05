import sys, math
input = sys.stdin.readline

d, h = map(float, input().split())

r = (d+10)/2
area = 2 * math.pi * r * h + math.pi*r*r
print(area)