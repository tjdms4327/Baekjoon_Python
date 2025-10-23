# bronzeII_17173
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
K = list(map(int, input().split()))

Sum = 0
for num in range(1, n+1):
    if any(num % i == 0 for i in K):
        Sum += num
print(Sum)