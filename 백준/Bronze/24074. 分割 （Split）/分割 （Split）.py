import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

max_val = max(A)
max_idx = A.index(max_val)
print(sum(A[:max_idx]))
print(sum(A[max_idx+1:]))