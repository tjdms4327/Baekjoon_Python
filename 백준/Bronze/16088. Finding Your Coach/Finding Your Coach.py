import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    l, r, n, m = map(int, input().split())
    if n == m:
        print('G')
    elif n-l <= m <= n+l:
        if n-r <= m <= n+r:
            print('E')
        else:
            print('L')
    elif n-r <= m <= n+r:
        print('R') 