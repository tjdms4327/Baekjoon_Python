# silverII_1699
import sys
input = sys.stdin.readline
from math import sqrt

n = int(input())

squareNum = []
for i in range(1, int(sqrt(n)+1)):
    squareNum.append(i*i)
    
dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = i
    for snum in squareNum:
        if i < snum:
            break
        dp[i] = min(dp[i], dp[i-snum]+1)

print(dp[n])