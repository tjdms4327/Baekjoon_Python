import sys
input = sys.stdin.readline

n = int(input())
P = [0] + list(map(int, input().split()))

dp = [0]*(n+1)
dp[1] = P[1]

for i in range(2, n+1):
    dp[i] = min(dp[i-x] +P[x] for x in range(1, i+1))
    
print(dp[n])