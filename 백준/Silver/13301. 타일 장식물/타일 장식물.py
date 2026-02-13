import sys
input = sys.stdin.readline

tile = [0]*81
tile[0] = tile[1] = 1
for i in range(2, 81):
    tile[i] = tile[i-1] + tile[i-2]
    
n = int(input())

x = y = 1
for i in range(1, n):
    if i % 2 == 0:
        x += tile[i]
    else:
        y += tile[i]
        
print(2*(x+y))