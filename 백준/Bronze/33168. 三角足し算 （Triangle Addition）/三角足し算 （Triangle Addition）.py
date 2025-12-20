import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

for _ in range(n-1):
    m = len(A)
    A = [A[i]+A[i+1] for i in range(m-1)]
    print(*A)