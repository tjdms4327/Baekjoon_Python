# bronzeII_14624
import sys
input = sys.stdin.readline

n = int(input())

if n % 2 == 0:
    print('I LOVE CBNU')
else:
    print('*'*n)
    print(' '*(n//2) + '*')
    for i in range(n//2-1, -1, -1):
        print(' '*i + '*' + ' '*(n-i*2-2) + '*')
    