import sys
input = sys.stdin.readline

r, c, w = map(int, input().split())

dp = [[0]*31 for _ in range(31)]
for i in range(1, 31):
    dp[i][1] = dp[i][i] = 1
    for j in range(2, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
        
ans = 0
for i in range(w):
    for j in range(i+1):
        ans += dp[r+i][c+j]
        
print(ans)