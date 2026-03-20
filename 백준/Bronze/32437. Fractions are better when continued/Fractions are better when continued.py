import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*(n+1)
dp[0] = (1,1) # (분모, 분자)
for i in range(1, n+1):
    b, a= dp[i-1]
    dp[i] = (a+b, b)
    # gcd(b, a+b) = gcd(a, b) = 1이므로 약분해서 넣을 필요X
    

print(dp[n][1])