import sys
input = sys.stdin.readline

v = [list(map(int, input().split())) for _ in range(3)]

def sol(v):
    if v[0][1] == v[1][1]:
        v = [[y, x] for x, y in v]

    v[0], v[1] = sorted(v[:2])

    if v[0][0] != v[1][0]:
        return 1
    if v[2][0] != v[0][0]:
        return 0
    return 2 if v[0][1] < v[2][1] < v[1][1] else 0

print(sol(v))
