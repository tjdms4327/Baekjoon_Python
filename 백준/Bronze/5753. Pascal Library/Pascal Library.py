import sys
input = sys.stdin.readline

while True:
    n, d = map(int, input().split())
    if n == d == 0: break

    attend = [list(map(int, input().split()))for _ in range(d)]
    for col in zip(*attend):
        if set(col) == {1}:
            print('yes')
            break
    else:
        print('no')