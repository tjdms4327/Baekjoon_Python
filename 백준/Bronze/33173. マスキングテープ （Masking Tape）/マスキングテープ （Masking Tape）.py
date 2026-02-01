import sys
input = sys.stdin.readline

h, w, q = map(int, input().split())

blocks = [[False]*w for _ in range(h)]
color = [[0]*w for _ in range(h)]

for _ in range(q):
    line = input().strip().split()
    if line[0]=='1':
        x, y, c = map(int, line[1:])
        x = int(x) ; y = int(y)
        for col in range(max(0, y-1), min(h, y+1)):
            for row in range(max(0, x-1), min(h, x+1)):
                if blocks[row][col] != True:
                    color[row][col] = int(c)
    else:
        x, y = map(int, line[1:])
        x = int(x) ; y = int(y)
        for col in range(max(0, y-1), min(h, y+1)):
            for row in range(max(0, x-1), min(h, x+1)):
                blocks[row][col] = True
    
for row in color:
    print(*row)