# bronzeII_32952
import sys
input = sys.stdin.readline

r, k, m = map(int, input().split())

halvings = m // k
for _ in range(halvings):
    r //= 2
    if r < 1:
        r = 0
        break
print(r)