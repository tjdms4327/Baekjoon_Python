import sys
input = sys.stdin.readline

board = [[0]*101 for _ in range(101)]

for _ in range(4):
    x0, y0, x1, y1 = map(int, input().split())
    for x in range(x0, x1):
        for y in range(y0, y1):
            board[x][y] = 1
            
ans = 0
for row in board:
    ans += sum(row)
    
print(ans)