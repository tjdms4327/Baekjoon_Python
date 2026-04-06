import sys
input = sys.stdin.readline

n = int(input())
P = [0] + [tuple(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
ans = INF
for first_color in range(3):
    dp = [[INF]*3 for _ in range(n+1)]
    dp[1][first_color] = P[1][first_color] # 첫 집 색 고정

    for i in range(2, n+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + P[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + P[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + P[i][2]

    # 마지막 집 색 != 첫 집 색
    for last_color in range(3):
        if last_color != first_color:
            ans = min(ans, dp[n][last_color])

print(ans)