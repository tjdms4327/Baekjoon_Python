import sys
input = sys.stdin.readline

n = int(input())
s = [list(input().strip()) for _ in range(n)]
t = [list(input().strip()) for _ in range(n)]

def rotate_right(a):
    return [list(row) for row in zip(*a[::-1])]

ans = float('inf')
cur = s

for rot in range(4):
    paint = 0
    for i in range(n):
        for j in range(n):
            if cur[i][j] != t[i][j]:
                paint += 1

    rotate_cost = min(rot, 4 - rot)
    ans = min(ans, rotate_cost + paint)

    cur = rotate_right(cur)

print(ans)
