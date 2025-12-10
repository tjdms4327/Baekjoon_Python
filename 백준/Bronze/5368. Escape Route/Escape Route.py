import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    matrix = [list(input().strip()) for _ in range(m)]
    
    for r in range(m):
        row = matrix[r]
        if 's' in row:
            x = r
            y = row.index('s')
    
    best = float('inf')
    for r in range(m):
        for c in range(m):
            if 'p' == matrix[r][c]:
                dist2 = (x-r)**2 + (y-c)**2
                if best > dist2:
                    best = dist2
                    best_c = [r, c]
    
    print(f'({x},{y}):({best_c[0]},{best_c[1]}):{best**0.5:.2f}')