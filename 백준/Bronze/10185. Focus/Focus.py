import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    p, q = map(int, input().split())
    f = 1 / (1 / p + 1/ q)
    print(f'f = {f:.1f}')