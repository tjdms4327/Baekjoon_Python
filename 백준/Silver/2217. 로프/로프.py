import sys
input = sys.stdin.readline

n = int(input())

max_w = [int(input()) for _ in range(n)]
max_w.sort()

best = 0
for i in range(n):
    weight = max_w[i] * (n - i)
    best = max(best, weight)
print(best)