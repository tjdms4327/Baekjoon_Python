# bronzeIII_11908
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
print(sum(nums[:-1]))