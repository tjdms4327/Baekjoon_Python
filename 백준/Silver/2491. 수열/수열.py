import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

inc = [1] * n
dec = [1] * n
max_len = 1

for i in range(1, n):
    if arr[i] >= arr[i-1]:
        inc[i] = inc[i-1] + 1
    if arr[i] <= arr[i-1]:
        dec[i] = dec[i-1] + 1
    max_len = max(max_len, inc[i], dec[i])
    
print(max_len)