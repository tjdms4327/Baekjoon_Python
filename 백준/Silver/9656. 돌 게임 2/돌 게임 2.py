import sys
input = sys.stdin.readline

n = int(input())

dp = [False] * (n+5)
dp[1] = False
dp[2] = True
dp[3] = False
dp[4] = True

for i in range(5, n+1):
    dp[i] = (not dp[i-1]) or (not dp[i-3])
    
print('SK' if dp[n] else 'CY')