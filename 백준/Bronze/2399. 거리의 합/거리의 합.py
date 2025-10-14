# bronzeII_2399
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

prefix_sum = [0]*(n+1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + nums[i]

result = 0
for i in range(n):
    result += nums[i]*i - prefix_sum[i]
print(result*2)