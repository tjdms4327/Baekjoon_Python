import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

for last in range(n-1, 0, -1):
    max_A = max(A[:last+1])
    max_index = A.index(max_A)
    if (last != max_index):
        A[last], A[max_index] = A[max_index], A[last]
        k -= 1
        
        if k == 0:
            break
        
if k > 0:
    print(-1)
else:
    print(*A)