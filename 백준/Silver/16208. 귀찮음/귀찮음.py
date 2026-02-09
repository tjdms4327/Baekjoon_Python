import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

tot = sum(A)
result = 0
for a in A[:-1]:
    tot -= a
    result += tot*a

print(result)