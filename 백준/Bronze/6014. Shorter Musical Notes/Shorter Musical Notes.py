import sys
input = sys.stdin.readline

def bisect_right(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left      

n, q = map(int, input().split())
B = [int(input()) for _ in range(n)]
prefix_sum = [0]*(n+1)
for i in range(1, 1+n):
    prefix_sum[i] = prefix_sum[i-1] + B[i-1]

for _ in range(q):
    t = int(input())
    print(bisect_right(prefix_sum, t))