import sys
input = sys.stdin.readline

n = int(input())
nums = [input().strip() for _ in range(n)]

for k in range(1, len(nums[0])+1):
    cand = set(x[-k:] for x in nums)
    if len(cand) == n:
        print(k)
        sys.exit()