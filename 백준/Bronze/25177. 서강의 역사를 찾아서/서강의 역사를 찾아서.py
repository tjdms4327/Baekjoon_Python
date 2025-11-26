import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
if n < m:
    A += [0]*(m-n)
B = list(map(int, input().split()))

diff = [B[i]-A[i] for i in range(m)]
print(max(max(diff),0))