import sys
input = sys.stdin.readline

for case in range(int(input())):
    M, N, x, y = map(int, input().split())

    res = -1
    for k in range(0, N):
        candidate = x + k * M
        if (candidate - y) % N == 0:
            res = candidate
            break
    print(res)