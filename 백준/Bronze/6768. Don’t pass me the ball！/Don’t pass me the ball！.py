import sys
input = sys.stdin.readline

from itertools import combinations

j = int(input())
if j < 4:
    print(0)
else:
    print(sum(1 for c in combinations(range(1, j), 3)))