import sys
input = sys.stdin.readline

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())

words = [input().strip() for _ in range(m)]

total_rows = u + m + d
total_cols = l + n + r
for i in range(total_rows):
    row = ""
    for j in range(total_cols):
        if u <= i < u + m and l <= j < l + n: # word 영역
            row += words[i - u][j - l]
        else:
            if (i + j) % 2 == 0:
                row += '#'
            else:
                row += '.'
    print(row)
