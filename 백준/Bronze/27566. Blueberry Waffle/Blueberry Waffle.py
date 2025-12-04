import sys
input = sys.stdin.readline

r, f = map(int, input().split())

angle = f * 180 / r
turn = round(angle / 180)

if turn % 2 == 0:
    print('up')
else:
    print('down')