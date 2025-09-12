import sys
input = sys.stdin.readline

pi = 3.14159

n = int(input())
V = 0
for _ in range(n):
    diagram = list(input().strip().split())
    if diagram[0] == 'C':
        r, h = float(diagram[1]), float(diagram[2])
        V = max(V, 1 / 3 * pi * r * r * h)
    elif diagram[0] == 'L':
        r, h = float(diagram[1]), float(diagram[2])
        V = max(V, pi * r * r * h)
    else: # 구('S')
        r = float(diagram[1])
        V = max(V, 4 / 3 * pi * (r ** 3))
    
print(f'{V:.3f}')