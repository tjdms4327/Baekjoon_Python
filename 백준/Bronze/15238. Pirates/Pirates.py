import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
s = input().strip()

counter = Counter(s)
max_i, freq = counter.most_common(1)[0]
print(max_i, freq)