# bronzeII_2979
import sys
input = sys.stdin.readline
from collections import Counter

a, b, c = map(int, input().split())
time = [tuple(map(int, input().split())) for _ in range(3)]

T = [0] * 101
for s, e in time:
    for t in range(s, e):
        T[t] += 1

counter = Counter(T)
result = counter[1]*a*1 + counter[2]*b*2 + counter[3]*c*3
print(result)