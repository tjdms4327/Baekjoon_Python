import sys
input = sys.stdin.readline

x, y = map(int, input().split())
n = int(input())
coordinate = ()
min_distance = float('inf')
for _ in range(n):
    xi, yi = map(int, input().split())
    distance = abs(x - xi) +abs(y - yi)
    if distance < min_distance:
        min_distance = distance
        coordinate = (xi, yi)
print(*coordinate)