import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0, 0
def solve(x, y, size):
    global white, blue
    
    color = paper[x][y]
    
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != color:
                half = size//2
                solve(x, y, half)
                solve(x, y+half, half)
                solve(x+half, y, half)
                solve(x+half, y+half, half)
                return
            
    if color == 0:
        white += 1
    else:
        blue += 1
        
        
solve(0, 0, n)
print(white)
print(blue)