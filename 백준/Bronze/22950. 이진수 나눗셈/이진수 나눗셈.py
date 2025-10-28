# bronzeI_22950
import sys
input = sys.stdin.readline

n = int(input())
m = int(input(), 2)
k = int(input()) ; k = 2**k

if m % k == 0:
    print('YES')
else:
    print('NO')