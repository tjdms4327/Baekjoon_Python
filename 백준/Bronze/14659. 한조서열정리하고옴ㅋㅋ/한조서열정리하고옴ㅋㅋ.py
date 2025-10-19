# bronzeI_14659
import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))

max_kill = 0
count = 0
highest = heights[0]
for i in range(1, n):
    if heights[i] < highest:
        count += 1
        max_kill = max(max_kill, count)
    else:
        highest = heights[i]
        count = 0

print(max_kill)