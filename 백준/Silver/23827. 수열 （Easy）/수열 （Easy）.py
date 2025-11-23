import sys
input = sys.stdin.readline
from itertools import combinations

MOD = 1000000007

n = int(input())
X = list(map(int, input().split()))

ans = sum(X)**2 
for x in X:
    ans -= x**2 
ans //= 2
print(ans%MOD)