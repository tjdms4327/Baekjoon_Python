import sys
input = sys.stdin.readline

n = int(input())
A = [0] + list(map(int, input().split()))

best = 0
cur = 0
for i in range(n+1):
    if A[i] == 1:
        cur += 1
    else:
        best = max(best, cur+1)
        cur = 0
best = max(best, cur+1)

print(best)