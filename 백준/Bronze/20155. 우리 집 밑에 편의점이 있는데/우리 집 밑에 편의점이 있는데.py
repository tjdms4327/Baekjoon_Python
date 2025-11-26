import sys
input = sys.stdin.readline
from collections import Counter

n, m = map(int, input().split())
X = list(map(int, input().split()))

counter = Counter(X)
print(max(counter.values()))