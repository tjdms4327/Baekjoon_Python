import sys
input = sys.stdin.readline

from math import ceil

x, y = map(int, input().split())
round = x / (y - x)
print(ceil(round) + 1)