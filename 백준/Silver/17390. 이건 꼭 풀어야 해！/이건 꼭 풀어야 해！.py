import sys, math
input = sys.stdin.readline

n, q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

prefix_sum = [0]*(n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1]+A[i-1]
    
for _ in range(q):
    i, j  = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])