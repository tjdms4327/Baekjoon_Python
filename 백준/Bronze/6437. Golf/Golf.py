import sys
input = sys.stdin.readline

case = 0
while True:
    p, s = map(int, input().split())
    if p == s == 0: break

    case += 1
    print(f'Hole #{case}')

    if s == 1:
        print('Hole-in-one.')
    elif s <= p-3:
        print('Double eagle.')
    elif s == p-2:
        print('Eagle.')
    elif s == p-1:
        print('Birdie.')
    elif s == p:
        print('Par.')
    elif s == p+1:
        print('Bogey.')
    elif s >= p+2:
        print('Double Bogey.')
    print()