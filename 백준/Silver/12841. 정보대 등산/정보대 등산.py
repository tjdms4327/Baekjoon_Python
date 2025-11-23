import sys
input = sys.stdin.readline

n = int(input())
cross = list(map(int, input().split()))
left = list(map(int, input().split()))
right = list(map(int, input().split()))

left_sum = [0] * (n+1) 
for i in range(1, n):
    left_sum[i] = left_sum[i-1] + left[i-1]
right_sum = [0] * (n+1) 
for i in range(n-2, -1, -1):
    right_sum[i] = right_sum[i+1] + right[i]

min_d = float('inf')
min_idx = 0
for i in range(n):
    dist = left_sum[i] + cross[i] + right_sum[i]
    if dist < min_d:
        min_d = dist
        min_idx = i + 1 
print(min_idx, min_d)