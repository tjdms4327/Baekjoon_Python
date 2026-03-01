import sys
input = sys.stdin.readline

x, y, z, n = map(int, input().split())

a, b, c = n, 1, 1
dx = x / a
dy = y / b
dz = z / c

for i in range(a):
    for j in range(b):
        for k in range(c):
            x1 = i * dx
            y1 = j * dy
            z1 = k * dz
            x2 = (i+1) * dx
            y2 = (j+1) * dy
            z2 = (k+1) * dz
            
            print(f"{x1:.8f} {y1:.8f} {z1:.8f} {x2:.8f} {y2:.8f} {z2:.8f}")