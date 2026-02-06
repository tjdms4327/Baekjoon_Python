import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

count = 0 
for i in range(1, n):
    if A[i-1] >= A[i]:
        if A[i-1] < A[i]+k:
            A[i] += k
            count += 1
        else:
            print(-1)
            sys.exit()
print(count)