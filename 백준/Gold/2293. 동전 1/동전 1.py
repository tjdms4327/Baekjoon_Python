import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
coins.sort(reverse = True)

dp = [0]*(k+1)
dp[0] = 1
for coin in coins:
    for amount in range(coin, k+1):
        dp[amount] += dp[amount-coin]
        
print(dp[k])