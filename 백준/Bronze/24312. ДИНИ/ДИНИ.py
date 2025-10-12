# bronzeIII_24312
import sys
input = sys.stdin.readline

watermelons = list(map(int, input().split()))

min_diff = float('inf')
for i in range(1, 1<<4):
    left = sum(watermelons[j] for j in range(4) if (i & (1<<j)))
    right = sum(watermelons) - left
    min_diff = min(min_diff, abs(left - right))
print(min_diff)