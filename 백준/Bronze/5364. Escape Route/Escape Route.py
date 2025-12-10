import sys
input = sys.stdin.readline

n = int(input())
x0, y0 = map(int, input().split())

best = float('inf')
for _ in range(n-1):
    x, y = map(int, input().split())
    dist = ((x0-x)**2 + (y0-y)**2)**0.5
    
    if best >= dist:
        best = dist
        coordinate = [x, y]

print(x0, y0)
print(*coordinate)
print(f'{best:.2f}')