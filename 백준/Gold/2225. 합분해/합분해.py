# goldV_2225
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n+1):
    for j in range(1, k+1):
        for t in range(0, i+1): # 마지막 정수로 쓸 값
            dp[i][j] += dp[i-t][j-1]
        dp[i][j] %= 1000000000
print(dp[n][k])