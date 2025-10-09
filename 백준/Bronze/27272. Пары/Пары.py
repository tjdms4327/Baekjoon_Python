# bronzeIII_27272
import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))

nums.sort()
print(nums[0]* nums[1] + nums[2] * nums[3])