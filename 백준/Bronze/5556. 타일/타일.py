# bronzeO_5556
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    layer = min(x-1, y-1, n-x, n-y) + 1
    color = (layer-1) % 3 + 1
    print(color)