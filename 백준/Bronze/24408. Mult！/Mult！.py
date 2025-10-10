# bronzeIII_24408
import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

find = nums[0]
check = False
for i in range(1, n):
    if check:
        find = nums[i]
        check = False
        continue
    if nums[i] % find == 0:
        print(nums[i])
        check = True