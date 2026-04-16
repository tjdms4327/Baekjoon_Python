import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print('*')
    sys.exit()
    
size = 4 * n - 3
board = [[' ']*size for _ in range(size)]

for i in range(n):
    start = 2 * i
    end = size - 1 - 2*i    
    
    # 위 아래
    for j in range(start, end+1):
        board[start][j] = '*'
        board[end][j] = '*'
        
    # 왼쪽 오른쪽
    for j in range(start, end+1):
        board[j][start] = '*'
        board[j][end] = '*'
        
for row in board:
    print(''.join(row))