import sys, math
input = sys.stdin.readline

w, h = map(int, input().split())
r = int(input())

area = w*h
area -= math.pi * r * r / 4
print(area) 