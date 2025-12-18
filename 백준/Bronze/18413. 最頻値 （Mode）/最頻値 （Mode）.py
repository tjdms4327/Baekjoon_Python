import sys
input = sys.stdin.readline
from collections import Counter

n, m = map(int, input().split())
A = list(map(int, input().split()))

count = Counter(A)
B = set()
for j in range(1, m+1):
    if j in count:
        B.add(count[j])
print(max(B))