import sys
input = sys.stdin.readline

player1 = int(input())
player2 = 2 if player1==1 else 1

coordinates = [tuple(map(int, input().split())) for _ in range(9)]


def end():
    for row in matrix:
        if len(set(row)) == 1 and row[0]!=0:
            return True
    for col in zip(*matrix):
        if len(set(col)) == 1 and col[0]!=0:
            return True
        
    if matrix[0][0]==matrix[1][1]==matrix[2][2] and matrix[0][0]!=0:
        return True
    elif matrix[0][2]==matrix[1][1]==matrix[2][0] and matrix[0][2]!=0:
        return True
    
    return False

matrix = [[0]*3 for _ in range(3)]
for i in range(9):
    x, y = coordinates[i]
    x -=1 ; y -= 1
    
    cur = player1 if i%2==0 else player2
    matrix[x][y] = cur
    
    if end():
        print(cur)
        sys.exit()

print(0)

