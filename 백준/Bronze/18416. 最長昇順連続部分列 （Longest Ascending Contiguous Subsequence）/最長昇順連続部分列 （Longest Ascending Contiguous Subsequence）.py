import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

max_len = 0
temp = 1
for i in range(1, n):
    if A[i-1] <= A[i]:
        temp += 1
    else:
        max_len = max(max_len, temp)
        temp = 1
max_len = max(max_len, temp)
print(max_len)