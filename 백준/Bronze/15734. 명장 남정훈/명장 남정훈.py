import sys
input = sys.stdin.readline

l, r, a = map(int, input().split())
small, big = min(l, r), max(l, r)

t = min(a, big - small)
small += t
a -= t
result = small * 2 + (a//2 *2 if a else 0)
print(result)