# bronzeI_20112
import sys
input = sys.stdin.readline

n = int(input())
row = [input().strip() for _ in range(n)]
col = [''.join(col) for col in zip(*row)]

if row == col:
    print('YES')
else:
    print('NO')