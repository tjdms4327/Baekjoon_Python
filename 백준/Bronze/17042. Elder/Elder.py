# bronzeIII_17042
import sys
input = sys.stdin.readline

now = input().strip()
have = set(now)

n = int(input())
for _ in range(n):
    a, b = input().strip().split()
    if now == b:
        now = a
        have.add(now)
print(now)
print(len(have))