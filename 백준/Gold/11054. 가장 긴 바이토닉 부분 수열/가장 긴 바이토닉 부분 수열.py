# goldIV_11054
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

increase = [1] * n
decrease = [1] * n
for i in range(1, n):
    for j in range(i):
        if A[i] > A[j]:
            increase[i] = max(increase[i], increase[j]+1)
    for k in range(n-1, n-i-1, -1):
        if A[n-i-1] > A[k]:
            decrease[n-i-1] = max(decrease[n-i-1], decrease[k]+1)

result = 0
for i in range(n):
    result = max(result, increase[i]+decrease[i])
print(result - 1)