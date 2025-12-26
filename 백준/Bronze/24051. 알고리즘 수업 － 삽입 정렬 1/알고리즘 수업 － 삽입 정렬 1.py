import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

for i in range(1, n):
    loc = i-1
    newItem = A[i]
    
    while (0<=loc and newItem<A[loc]):
        A[loc+1] = A[loc]
        k -= 1
        if k == 0:
            print(A[loc+1])
            sys.exit()
        loc -= 1
        
    if (loc+1 != i):
        A[loc+1] = newItem
        k -= 1
        if k == 0:
            print(A[loc+1])
            break

print(-1)

    