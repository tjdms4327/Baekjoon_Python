import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    tile = list(map(int, input().split()))
    
    if 2 in tile:
        idx = tile.index(2)
        direction = 1
    elif 3 in tile:
        idx = tile.index(3)
        direction = -1    
    
    count_yellow = 0
    for i in range(n):
        idx += direction
        
        if idx < 0:
            idx = 1
            direction = 1
        elif idx >= m:
            idx = m - 2
            direction = -1
            
        if tile[idx] == 0:
            count_yellow += 1
            
    print(count_yellow)