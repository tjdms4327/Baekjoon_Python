# silverI_11057
import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for _ in range(n)]
for i in range(10):
    dp[0][i] = 1
for i in range(1, n):
    temp = 0
    for j in range(10):
        temp += dp[i-1][j] # j는 마지막 자리
        temp %= 10007
        dp[i][j] = temp
print(sum(dp[n - 1]) % 10007)