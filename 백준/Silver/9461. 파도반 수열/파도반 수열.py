# silverIII_9461
import sys
input = sys.stdin.readline

dp = [0] * (101)
dp[1]= dp[2] = dp[3] = 1
for i in range(1, 100-2):
    dp[i+3] = dp[i] + dp[i+1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])