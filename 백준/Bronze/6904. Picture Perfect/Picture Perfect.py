import sys, math
input = sys.stdin.readline

while True:
    c = int(input())
    if c == 0:
        break
    
    best = [float('inf')]
    for i in range(1, math.isqrt(c)+1):
        if c % i == 0:
            p = 2 * (i + c//i)
            if best[0] > p:
                best = [p, i, c//i]
    
    p, w, h = best
    print(f'Minimum perimeter is {p} with dimensions {w} x {h}')