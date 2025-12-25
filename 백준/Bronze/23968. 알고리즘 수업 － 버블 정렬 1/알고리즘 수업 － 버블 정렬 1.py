import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

for last in range(n, 1, -1):
    for i in range(last - 1):
        if A[i] > A[i + 1]:
            k -= 1
            if k == 0:
                print(min(A[i], A[i+1]), max(A[i], A[i+1]))
                sys.exit()
            A[i], A[i+1] = A[i+1], A[i]

print(-1)
