import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    n = int(input())
    
    best = 10**9
    for a in range(1, int(n**(1/3)) + 2):
        if n % a != 0:
            continue
        Na = n // a
        for b in range(a, int((Na)**0.5) + 2):
            if Na % b != 0:
                continue
            c = Na // b
            
            area = 2 * (a*b + b*c + c*a)
            if area < best:
                best = area
                
    print(best)