import sys, math
input = sys.stdin.readline

def calculate_area(r):
    return math.pi * r * r

t = int(input())
for case in range(1, 1+t):
    r, a, b = map(int, input().split())
    
    area = calculate_area(r)
    while r != 0:
        r *= a
        area += calculate_area(r)
        r //= b
        if r == 0: break
        area += calculate_area(r)
    
    print(f'Case #{case}: {area}')