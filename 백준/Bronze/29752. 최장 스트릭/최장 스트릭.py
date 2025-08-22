import sys
input = sys.stdin.readline

from itertools import groupby

n = int(input())
days = list(map(int, input().split()))


result = [len(list(g)) for k, g in groupby(days, key=lambda x: x != 0) if k]
print(max(result, default = 0))