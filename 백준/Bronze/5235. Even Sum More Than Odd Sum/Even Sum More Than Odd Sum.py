import sys
input = sys.stdin.readline

for case in range(int(input())):
    K = list(map(int, input().split()))

    even = sum(n for n in K[1:] if n % 2 == 0)
    odd = sum(K[1:]) - even
    if even > odd:
        print('EVEN')
    elif even == odd:
        print('TIE')
    else:
        print('ODD')