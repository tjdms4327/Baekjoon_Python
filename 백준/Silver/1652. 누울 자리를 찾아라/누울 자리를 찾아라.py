import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(input().strip()) for _ in range(n)]

w, h = 0, 0
for row in matrix:
    cnt = 0
    for r in row:
        if r == '.':
            cnt += 1
        else:
            if cnt >= 2:
                w += 1
            cnt = 0
    if cnt >= 2:
        w += 1
        
for col in zip(*matrix):
    cnt = 0
    for c in col:
        if c == '.':
            cnt += 1
        else:
            if cnt >= 2:
                h += 1
            cnt = 0
    if cnt >= 2:
        h += 1
        
print(w, h)