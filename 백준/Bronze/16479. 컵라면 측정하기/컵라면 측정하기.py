import sys
input = sys.stdin.readline

from math import sqrt

k=int(input())
d1,d2=map(int, input().split())
d=(d1-d2)/2

print(k**2-d**2)