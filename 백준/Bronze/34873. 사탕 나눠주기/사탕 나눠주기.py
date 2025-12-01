import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
A = list(map(int, input().split()))

counter = Counter(A)
if max(counter.values()) >= 3:
    print('No')
else:
    print('Yes')