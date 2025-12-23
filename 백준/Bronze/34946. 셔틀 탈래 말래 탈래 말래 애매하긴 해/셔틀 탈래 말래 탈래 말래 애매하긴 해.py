import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())

shuttle = (a+b) <= d
walk = c <= d

if shuttle and walk:
    print('~.~')
elif shuttle:
    print('Shuttle')
elif walk:
    print('Walk')
else:
    print('T.T')