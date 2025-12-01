import sys
input = sys.stdin.readline

y, c, p = map(int, input().split())
c //= 2
print(min(y, c, p))