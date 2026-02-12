import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    
    best, best_h = [],  0
    for _ in range(n):
        name, h = input().strip().split()
        h = float(h)
        
        if best_h < h:
            best = [name]
            best_h = h
        elif best_h == h:
            best.append(name)
            
    print(*best)