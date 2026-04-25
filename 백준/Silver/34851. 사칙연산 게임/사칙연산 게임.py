import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

curr = nums[0]
MOD = 10**9 + 7

for i in range(N):
    x = nums[i+1]
    
    if x == 1 or (i == 0 and curr == 1):
        curr = (curr + x) % MOD
    else:
        curr = (curr * x) % MOD

print(curr)