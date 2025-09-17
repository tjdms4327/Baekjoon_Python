import sys
input = sys.stdin.readline

a, b = map(float, input().split())
n = int(input())
for _ in range(n):
    z, q = input().strip().split()
    
    if q == 'A':
        z = float(z) * (b/a)
    else:
        z = float(z) * (a/b)
    print(z)