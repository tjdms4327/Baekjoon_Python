import sys
input = sys.stdin.readline

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]

count = [0]*5  # 0~4대 부수는 경우

for i in range(r-1):
    for j in range(c-1):
        block = [
            matrix[i][j],
            matrix[i][j+1],
            matrix[i+1][j],
            matrix[i+1][j+1]
        ]
        
        if '#' in block:
            continue
        
        x_cnt = block.count('X')
        count[x_cnt] += 1

for i in range(5):
    print(count[i])
