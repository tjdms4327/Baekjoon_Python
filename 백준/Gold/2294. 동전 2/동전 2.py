import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
coins.sort(reverse = True)

INF = 10001
dp = [INF]*(k+1)
dp[0] = 0

for coin in coins:
    for amount in range(coin, k+1):
        dp[amount] = min(dp[amount], dp[amount-coin]+1)
        
print(dp[k] if dp[k]!=INF else -1)
