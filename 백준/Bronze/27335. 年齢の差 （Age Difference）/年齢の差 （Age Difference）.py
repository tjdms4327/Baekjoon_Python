import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

for i in range(n):
    best = 0
    for j in range(n):
        if i != j:
            x = abs(A[i] - A[j])
            best = max(best, x)
    print(best)