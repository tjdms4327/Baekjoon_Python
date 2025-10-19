# bronzeI_1292
import sys
input = sys.stdin.readline

nums = [0]
for i in range(1, 45+1):
    nums.extend([i]*i)
    
a, b = map(int, input().split())

prefix_sum = [0] * (b+1)
for i in range(1, b+1):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]
print(prefix_sum[b] - prefix_sum[a-1])