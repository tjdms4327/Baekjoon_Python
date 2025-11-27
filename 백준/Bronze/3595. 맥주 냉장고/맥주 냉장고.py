import sys
input = sys.stdin.readline

n = int(input())

best_surface = float('inf')
best = (1, n, 1)
a = 1
while a * a * a <= n:
    if n % a == 0:
        n1 = n // a
        b = a
        while b * b <= n1:
            if n1 % b == 0:
                c = n1 // b
                surface = 2 * (a*b + b*c + c*a)
                if surface < best_surface:
                    best_surface = surface
                    best = (a, b, c)
            b += 1
    a += 1

print(*best)
