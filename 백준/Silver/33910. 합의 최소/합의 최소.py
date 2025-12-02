import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

for i in range(n-2, -1, -1):
    if A[i] > A[i+1]:
        A[i] = A[i+1]
print(sum(A))