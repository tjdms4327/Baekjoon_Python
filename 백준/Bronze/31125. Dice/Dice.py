import sys
input=sys.stdin.readline

b=int(input())
for _ in range(b):
    s, n, f, m=map(int, input().split())
    if n+m<=s<=n*f+m:
        print('YES')
    else: print('NO')
