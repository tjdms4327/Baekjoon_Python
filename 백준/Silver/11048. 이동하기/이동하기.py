import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dp =[[0]*m for _ in range(n)]
dp[0][0] = grid[0][0]

for i in range(n):
    for j in range(m):
        if i == j == 0:
            continue
        
        up = dp[i-1][j] if i > 0 else 0
        left = dp[i][j-1] if j > 0 else 0
        diag = dp[i-1][j-1] if i > 0 and j > 0 else 0
        
        dp[i][j] = max(up, left, diag) + grid[i][j]
        
print(dp[n-1][m-1])