import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
for _ in range(n):
    cards = list(input().strip().split())

    ranks = [c[0] for c in cards]
    cnt = Counter(ranks)
    print(max(cnt.values()))
    