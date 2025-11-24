import sys
input = sys.stdin.readline
from collections import Counter

n, m = map(int, input().split())
A = [int(input()) for _ in range(n)]
B = [int(input()) for _ in range(m)]

count = [0] * (n+1)
for i in range(m):
    for j in range(n):
        if A[j] <= B[i]:
            count[j+1] += 1
            break

max_count = max(count)
print(count.index(max_count))