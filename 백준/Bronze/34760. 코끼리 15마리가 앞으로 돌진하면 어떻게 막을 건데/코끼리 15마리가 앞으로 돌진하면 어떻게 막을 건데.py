import sys
input = sys.stdin.readline

A = list(map(int, input().split()))

max_A = max(A)
if A.index(max_A) != 14:
    max_A += 1
print(max_A)