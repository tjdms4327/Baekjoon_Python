# silverIII_2579
import sys
input = sys.stdin.readline

n = int(input())
stairs = [int(input()) for _ in range(n)]

dp = [0] * n
for i in range(n):
  if i == 0:
    dp[0] = stairs[0]
  elif i == 1:
    dp[1] = stairs[0] + stairs[1]
  else:
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
print(dp[-1])