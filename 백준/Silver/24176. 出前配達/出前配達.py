# silverV_24176
import sys
input = sys.stdin.readline

while True:
    h, w = map(int, input().split())
    if h == w == 0:
        break
    
    matrix = [list(map(int, input().strip())) for _ in range(h)]

    rows = [sum(row) for row in matrix]
    total = sum(rows)
    r = sum((i+1)*rows[i] for i in range(h)) / total

    cols = [sum(list(col)) for col in zip(*matrix)]
    c = sum((i+1)*cols[i] for i in range(w)) / total

    print(r, c)