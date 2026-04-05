import sys
input = sys.stdin.readline

n, b = map(int, input().split())

if n <= (1<<(b+1))-1:
    print('yes')
else:
    print('no')