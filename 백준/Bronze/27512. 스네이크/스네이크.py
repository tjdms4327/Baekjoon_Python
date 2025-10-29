# bronzeII_27512
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n == 1 or m == 1:
    print(1)
elif n*m % 2 == 1:
    print(n*m - 1)
else:
    print(n*m)