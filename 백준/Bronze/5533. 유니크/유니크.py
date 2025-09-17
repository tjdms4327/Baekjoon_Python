import sys
input = sys.stdin.readline
from collections import Counter

n = int(input()) # 참가자 수
result = [0] * n
nums = [list(map(int, input().split())) for _ in range(n)]

for col in zip(*nums):
    round = Counter(col)
    for i in range(n):
        if round[col[i]] == 1:
            result[i] += col[i]
print(*result, sep = '\n')