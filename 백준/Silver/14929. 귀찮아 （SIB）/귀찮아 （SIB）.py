import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
X = list(map(int, input().split()))

ans = sum(X)**2
for x in X:
    ans -= x**2
print(ans//2)