import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())
t = int(input())

manhattan = abs(a - c) + abs(b - d)
if manhattan <= t and (t - manhattan) % 2 == 0:
    print('Y')
else:
    print('N')