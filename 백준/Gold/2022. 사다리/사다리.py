import sys
input = sys.stdin.readline

from math import sqrt

x, y, c = map(float, input().split())
left = 0.0
right = min(x, y)
eps = 1e-6

while right - left > eps:
    mid = (left + right) / 2.0
    hx = sqrt(x**2 - mid**2)
    hy = sqrt(y**2 - mid**2)
    
    h_cross = (hx * hy) / (hx + hy)
    if h_cross > c:
        left = mid
    else:
        right = mid
print(f"{mid:.3f}")