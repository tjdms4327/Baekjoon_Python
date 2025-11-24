import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [int(input()) for _ in range(n)]

for i in range(1, 1+m):
    for j in range(n-1):
        if A[j] % i > A[j+1] % i:
            A[j], A[j+1] = A[j+1],  A[j]

print(*A, sep='\n')