import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    B = [0]*n
    for i in range(1, n):
        B[i] = sum(1 for k in range(i) if A[k]<=A[i])
    print(sum(B))