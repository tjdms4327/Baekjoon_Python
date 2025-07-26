def draw_star(x, y, size):
    if size == 3:
        arr[x][y+2] = '*'
        arr[x+1][y+1] = '*'
        arr[x+1][y+3] = '*'
        for i in range(5):
            arr[x+2][y+i] = '*'
    else:
        half = size // 2
        draw_star(x, y + half, half)
        draw_star(x + half, y, half)
        draw_star(x + half, y + size, half)

n = int(input())
width = 2*n - 1
arr = [[' ']*width for _ in range(n)]

draw_star(0, 0, n)
for line in arr:
    print(''.join(line))