import sys
input = sys.stdin.readline

s = set(input().strip())
rotate = set('IOSHZXN')

if s <= rotate:
    print('YES')
else:
    print('NO')