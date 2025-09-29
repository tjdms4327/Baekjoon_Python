# bronzeIII_9838
import sys
input = sys.stdin.readline

n = int(input())
nums = [0] * (n+1)
for i in range(1, n+1):
    k = int(input())
    nums[k] = i
print(*nums[1:], sep='\n')