import sys
input = sys.stdin.readline

l, c, n = map(int, input().split())
for _ in range(c):
    s, p = map(int, input().split())
    print(s + abs(n-p))