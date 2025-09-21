import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from fractions import Fraction
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

n = int(input().strip())
A = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, p, q = map(int, input().split())
    A[a].append((b, p, q))
    A[b].append((a, q, p))

visited = [False] * n
D = [Fraction(0, 1) for _ in range(n)]

def dfs(v):
    visited[v] = True
    for nxt, p, q in A[v]:
        if not visited[nxt]:
            D[nxt] = D[v] * Fraction(q, p)
            dfs(nxt)

D[0] = Fraction(1, 1)
dfs(0)

L = 1
for frac in D:
    L = lcm(L, frac.denominator)

vals = [int(frac * L) for frac in D]
g = vals[0]
for v in vals[1:]:
    g = math.gcd(g, v)

for v in vals:
    print(v // g, end=' ')