import sys
input = sys.stdin.readline

n, e = map(int, input().split())
prop = list(map(float, input().split()))
P = [[prop[0], prop[1]], # -> good
     [prop[2], prop[3]]] # -> bad


dp = [[0.0, 0.0] for _ in range(n+1)] # [good, bad]
dp[0][e] = 1.0

for i in range(1, n+1):
    dp[i][0] = dp[i-1][0]*P[0][0] + dp[i-1][1]*P[1][0]
    dp[i][1] = dp[i-1][0]*P[0][1] + dp[i-1][1]*P[1][1]
    

good = round(dp[-1][0] * 1000)
bad  = round(dp[-1][1] * 1000)
print(good)
print(bad)