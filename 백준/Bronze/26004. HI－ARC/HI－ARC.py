import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
s = Counter(k for k in input().strip() if k in 'HIARC')

if len(s) == 5:
    print(min(s.values()))
else: print(0)