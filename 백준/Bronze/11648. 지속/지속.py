import sys
input = sys.stdin.readline

from math import prod

n=input().strip()

cnt = 0
while len(n) > 1:
    n = str(prod(int(c) for c in n))
    cnt+=1
print(cnt)