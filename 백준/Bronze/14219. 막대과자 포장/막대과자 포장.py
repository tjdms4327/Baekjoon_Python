# bronzeII_14219
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if (m*n) % 3 == 0:
    print('YES')
else:
    print('NO')