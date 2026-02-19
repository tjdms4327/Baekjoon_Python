import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
H = [list(map(int, input().split())) for _ in range(n)]

best = float('inf')
best_h = -1

for h in range(257): 
    box = b
    time = 0
    for r in range(n):
        for c in range(m):
            diff = H[r][c] - h
            if diff > 0:  
                time += 2 * diff
                box += diff
            elif diff < 0:
                time += -diff
                box += diff  
            
    if box >= 0:
        if time <= best:
            best = time
            best_h = h

print(best, best_h)
