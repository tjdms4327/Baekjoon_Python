import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

min_move = abs(a) + abs(b)

if c>=min_move and (c-min_move) % 2 == 0:
    print('YES')
else:
    print('NO')