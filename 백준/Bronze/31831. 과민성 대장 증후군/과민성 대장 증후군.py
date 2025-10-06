# bronzeIII_31831
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))

prefix_sum = [0] * (n+1)
result = [0] * (n+1)
for i in range(1, n+1):
    prefix_sum[i] = max(0, prefix_sum[i-1] + A[i])
    if prefix_sum[i] >= m:
        result[i] = 1
print(sum(result))