import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

ans = 1
last = A[0] % 2
for i in range(1, n):
    if A[i] % 2 != last:
        ans += 1
        last = A[i]%2
print(ans)