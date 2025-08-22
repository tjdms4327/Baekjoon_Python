import sys
input = sys.stdin.readline

a, d, k = map(int, input().split())

k -= a
if k % d != 0:
    print('X')
else:
    n = k // d + 1
    if n >= 1:
        print(n)
    else:
        print('X')