import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    lst = list(map(int, input().split()))
    
    k = lst[0]
    row, col = [0]*9, [0]*9
    safe = True
    for i in range(1, 2*k, 2):
        x = lst[i]
        y = lst[i+1]
        
        if row[y]==1 or col[x]==1:
            print('NOT SAFE')
            safe = False
            break
        row[y] = 1
        col[x] = 1
        
    if not safe:
        continue
    else:
        print('SAFE')
    