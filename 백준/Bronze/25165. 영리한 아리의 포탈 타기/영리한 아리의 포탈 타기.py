# bronzeII_25165
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
Ac, d = map(int, input().split())
Sr, Sc = map(int, input().split())

if Sr < n:
    print("NO...")
else:
    if d == 0:
        if n % 2 == 0:
            print('NO...')
        else:
            print('YES!')
    else:
        if n % 2 == 1:
            print('NO...')
        else:
            print('YES!')