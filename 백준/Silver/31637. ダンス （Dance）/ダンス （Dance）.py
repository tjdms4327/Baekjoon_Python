import sys
input = sys.stdin.readline

n, d = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

for i in range(0, 2*n, 2):
    if A[i+1] - A[i] > d:
        print('No')
        sys.exit()
print('Yes')