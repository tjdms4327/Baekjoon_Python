import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

up = [0] * n
down = [0] * n

for i in range(1, n):
    if A[i] > A[i-1]:
        up[i] = up[i-1] + 1

for i in range(n-2, -1, -1):
    if A[i] > A[i+1]:
        down[i] = down[i+1] + 1

answer = 1
for i in range(n):
    answer = max(answer, up[i] + down[i] + 1)
print(answer)