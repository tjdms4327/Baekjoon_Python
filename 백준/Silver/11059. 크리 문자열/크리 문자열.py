import sys
input=sys.stdin.readline

s=input().strip()
n=len(s)

prefix_sum=[0]*(n+1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + int(s[i])

max_len = 0
for length in range(n, 1, -1):  # 길이 긴 것부터
    if length % 2 != 0:
        continue 
        
    for i in range(n - length + 1):  # 시작 위치
        mid = i + length // 2
        j = i + length
        left = prefix_sum[mid] - prefix_sum[i]
        right = prefix_sum[j] - prefix_sum[mid]
        if left == right:
            max_len = length
            break 
    if max_len:
        break

print(max_len)