import sys
input = sys.stdin.readline

c, n = map(int, input().split())

if c > n:
    print(0)
elif c == n:
    print(c)
else:
    print(c+1)