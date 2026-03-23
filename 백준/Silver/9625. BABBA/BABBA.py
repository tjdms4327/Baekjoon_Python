import sys
input = sys.stdin.readline

k = int(input())

dp = [(0,0)]*(k+1)
dp[0] = (1,0)
dp[1] = (0,1)
for i in range(2, k+1):
    a, b = dp[i-1]
    cur_a, cur_b = b, a+b
    dp[i] = (cur_a, cur_b)
    
print(*dp[k])