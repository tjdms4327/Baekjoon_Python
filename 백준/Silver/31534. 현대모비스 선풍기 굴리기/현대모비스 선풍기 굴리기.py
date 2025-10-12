# silverIV_31534
import sys, math
input = sys.stdin.readline

PI = math.pi

a, b, h = map(int, input().split())

if b-a <= 0:
    print(-1)
    exit()

x = b*h/(b-a)
double_small_l = a**2 + (x-h)**2
double_big_l = b**2+ x**2
print(PI*(double_big_l - double_small_l))