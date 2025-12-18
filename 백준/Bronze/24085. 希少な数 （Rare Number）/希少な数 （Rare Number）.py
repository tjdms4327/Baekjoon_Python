import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
A = list(map(int, input().split()))

counts = Counter(A)
min_count = min(counts.values())
for val in sorted(counts):
    if counts[val] == min_count:
        print(val)
        break