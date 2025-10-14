# bronzeII_1434
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for book in B:
    for i in range(n):
        if A[i] >= book:
            A[i] -= book
            break

    for i in range(len(A)-1, -1, -1):
        if A[i] <= 0:
            del A[i]

print(sum(A))
