import sys
input = sys.stdin.readline

n, k, x, y = map(int, input().split())
count = 0
for _ in range(n):
    xi, yi = map(int, input().split())
    distance = ((xi - x) ** 2 + (yi - y) ** 2) ** 0.5
    if distance > k: 
        count += 1
print(count)