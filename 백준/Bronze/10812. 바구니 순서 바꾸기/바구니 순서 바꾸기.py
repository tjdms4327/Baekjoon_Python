# bronzeII_10812
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = [0] + list(range(1, n+1))

for _ in range(m):
    i, j, k = map(int, input().split())
    basket[i:j+1] = basket[k:j+1] + basket[i:k]
print(*basket[1:])