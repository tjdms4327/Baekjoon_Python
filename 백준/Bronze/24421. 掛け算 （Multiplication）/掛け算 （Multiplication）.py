import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
A = list(input().strip().split())

count = 0
for x, y, z in combinations(A, 3):
    if int(x) * int(y) == int(z):
        count += 1
print(count)