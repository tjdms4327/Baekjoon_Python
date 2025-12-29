import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
    m -= (A[i]-1)

if m > 0:
    print('OUT')
else:
    print('DIMI')