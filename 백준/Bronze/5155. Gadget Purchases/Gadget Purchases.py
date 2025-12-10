import sys
input = sys.stdin.readline
from collections import Counter

k = int(input())
for case in range(1, k+1):
    n, m = map(int, input().split())
    machine = [list(map(int, input().split())) for _ in range(m)]
    patient = [int(input()) for _ in range(n)]
    
    count = Counter(patient)
    profitable = []

    for idx in range(1, m+1):
        pi, ci, ui, ri = machine[idx-1]
        uses = min(ui, count[idx])
        profit = uses * (ri - ci) - pi

        if profit > 0:
            profitable.append(idx)

    print(f"Data Set {case}:")
    for x in sorted(profitable):
        print(x)
    print()