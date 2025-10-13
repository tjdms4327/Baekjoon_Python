# bronzeII_5617
import sys

triangle = [0] * 3
for line in sys.stdin.read().splitlines():
    a, b, c = sorted(map(int, line.split()))
    if a + b <= c:
        break
    
    A, B, C = a**2, b**2, c**2
    if A + B == C:
        triangle[0] += 1
    elif A + B > C:
        triangle[1] += 1
    else:
        triangle[2] += 1

print(sum(triangle), *triangle)