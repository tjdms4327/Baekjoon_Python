# silverIV_5591
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]

window_sum = sum(A[:k])
max_sum = window_sum
for i in range(k, n):
    window_sum += A[i] - A[i-k] 
    max_sum = max(max_sum, window_sum)
print(max_sum)