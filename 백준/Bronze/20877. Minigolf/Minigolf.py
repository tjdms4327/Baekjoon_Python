# bronzeIII_20877
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

count = 0
for i in range(n):
    if nums[i] > 7:
        nums[i] = 7
    if i % 2 == 0:
        count += (nums[i] - 2)
    else:
        count += (nums[i] - 3)
print(count)