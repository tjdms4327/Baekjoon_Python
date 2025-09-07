import sys
input = sys.stdin.readline

n = float(input())
if n <= 30:
    print(f'{n/2:.1f}')
else:
    print(f'{15 + 1.5*(n-30):.1f}')