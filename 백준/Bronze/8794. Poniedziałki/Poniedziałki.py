import sys
input = sys.stdin.readline

z = int(input())
for _ in range(z):
    n, m, l = map(int, input().split())
    ans = 0
    n -= (m - l + 1)
    if n > 0:
        ans += n // m
        if n % m:
            ans += 1
    if l == 1:
        ans += 1
    print(ans)
