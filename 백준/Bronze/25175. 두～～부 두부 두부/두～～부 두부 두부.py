import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
res = (m + k - 3) % n
if res == 0:
    res = n
print(res)