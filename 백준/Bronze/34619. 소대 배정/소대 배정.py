# bronzeII_34619
import sys
input = sys.stdin.readline

a, b, n, k = map(int, input().split())

for i in range(1, a+1):
    for j in range(1, b+1):
        if k <= n:
            print(i, j)
            sys.exit()
        k -= n