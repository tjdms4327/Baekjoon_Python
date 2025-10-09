# bronzeIII_28598
import sys
input = sys.stdin.readline

x1, x2, n = map(int, input().split())
if (x1-x2) % 2 == 0 and (x1-x2)/2 >= n:
    print('YES')
else:
    print('NO')