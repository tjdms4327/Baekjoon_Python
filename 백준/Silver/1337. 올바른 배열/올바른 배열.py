import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(int(input()) for _ in range(n))

best = 0
left = 0

for right in range(n):
    while nums[right] - nums[left] > 4:
        left += 1
    best = max(best, right - left + 1)

print(5 - best)