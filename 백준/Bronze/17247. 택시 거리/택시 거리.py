n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

x, y = -1, -1
for row in range(n):
    for col in range(m):
        if matrix[row][col] == 1:
            if x!= -1:
                print(abs(x-row) + abs(y-col))
                exit()
            else:
                x = row
                y = col