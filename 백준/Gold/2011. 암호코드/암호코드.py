# goldV_2011
import sys
input = sys.stdin.readline

a = list(map(int, input().strip()))
l = len(a)

dp = [0] * (l+1)
if a[0] == 0:
    print(0)
else :
    a = [0] + a
    dp[0] = 1
    dp[1] = 1

    for i in range(2, l+1):
        cur = a[i]
        cur2 = a[i-1] * 10 + a[i]
        if 1<= cur <= 9:
            dp[i] += dp[i-1]
        if 10 <= cur2 <= 26:
            dp[i] += dp[i-2]
        dp[i] %= 1000000

    print(dp[l])