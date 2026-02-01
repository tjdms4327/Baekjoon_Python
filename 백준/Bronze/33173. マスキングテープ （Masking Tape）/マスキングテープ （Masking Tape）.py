import sys
input = sys.stdin.readline

h, w, q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(q)]

ans = [[0]*w for _ in range(h)]
blocked = [[False]*w for _ in range(h)]

for q in queries:
    if q[0] == 1:
        _, x, y, c = q
        x -= 1
        y -= 1
        for i in range(x, x+2):
            for j in range(y, y+2):
                if not blocked[i][j]:
                    ans[i][j] = c
    else:
        _, x, y = q
        x -= 1
        y -= 1
        for i in range(x, x+2):
            for j in range(y, y+2):
                blocked[i][j] = True

for i in range(h):
    print(*ans[i])
