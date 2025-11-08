# silverI_2156
import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]

dp = [0] * n
for i in range(n):
    if i == 0:
        dp[i] = wines[i]
    elif i == 1:
        dp[i] = dp[i-1] + wines[i]
    elif i == 2:
        dp[i] = max(dp[i-1], wines[i-1]+wines[i], dp[i-2]+wines[i])
    else:
        dp[i] = max(dp[i-1], dp[i-3]+wines[i-1]+wines[i], dp[i-2]+wines[i])
print(dp[-1])