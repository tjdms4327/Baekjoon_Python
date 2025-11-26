import sys
input = sys.stdin.readline

n = int(input())
x0, x1, y0, y1 = -float('inf'), float('inf'), -float('inf'), float('inf')
for _ in range(n):
    x, y, d = input().strip().split()
    x, y = int(x), int(y)
    
    if d == 'R':
        x0 = max(x0, x+1)
    elif d == 'L':
        x1 = min(x1, x-1)
    if d == 'U':
        y0 = max(y0, y+1)
    elif d == 'D':
        y1 = min(y1, y-1)
        
if float('inf') in [x0, x1, y0, y1]\
    or -float('inf') in [x0, x1, y0, y1]:
        print('Infinity')
else:
    print((x1-x0+1)*(y1-y0+1))
    