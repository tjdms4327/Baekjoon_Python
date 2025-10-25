# bronzeII_32279
import sys
input = sys.stdin.readline

n = int(input())
p, q, r, s = map(int, input().split())
a1 = int(input())

A = [0] * (n+1)
A[1] = a1
for i in range(2, n+1):
    if i%2==1:
        A[i] = A[i//2]*r + s
    else:
        A[i] = A[i//2]*p + q
print(sum(A[1:]))