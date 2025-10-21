# bronzeI_9455
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]
    
    move_count = 0
    for col in zip(*matrix):
        bottom = m-1
        
        for i in range(m-1, -1, -1):
            if col[i] == 1:
                move_count += bottom - i
                bottom -= 1
    print(move_count)