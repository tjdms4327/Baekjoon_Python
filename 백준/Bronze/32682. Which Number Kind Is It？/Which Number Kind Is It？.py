import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    odd = n%2==1
    square = math.isqrt(n)**2==n
    if odd and square:
        print('OS')
    elif odd:
        print('O')
    elif square:
        print('S')
    else:
        print('EMPTY')