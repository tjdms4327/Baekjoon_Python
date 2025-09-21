# bronzeIII_20473
import sys
input = sys.stdin.readline

n = int(input())
q, r = divmod(n, 3)
if r % 3 == 0 or n % 3 == 2:
    print(r//2, q)
else:
    print(r//2 + 2, q - 1)