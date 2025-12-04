import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b, c = map(float, input().split())
    
    temp = (b**2 - 4*a*c)**0.5
    x1 = (-b+temp) / (2*a)
    x2 = (-b-temp) / (2*a)
    print(f'{x1:.3f}, {x2:.3f}')