import sys
input = sys.stdin.readline

n = int(input())

min_v = float('inf')
max_v = 0
tot = 0
for _ in range(n):
    a, b = map(int, input().split())
    min_v = min(min_v, a/b)
    max_v = max(max_v, a/b)
    tot += a/b
print(min_v, max_v, tot)