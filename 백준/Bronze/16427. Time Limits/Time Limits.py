import sys
input = sys.stdin.readline

from math import ceil

n, s = map(int, input().split())
M = list(map(int, input().split()))

time = max(M) * s / 1000 # 초 기준
print(ceil(time))