import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
Z = [list(map(int, input().split())) for _ in range(m)]
B = [col for col in zip(*Z)]

result = [[0]*k for _ in range(n)]
for row in range(n):
    for col in range(k):
        X = A[row]
        Y = B[col]
        
        result[row][col] = sum(X[x]*Y[x] for x in range(m))
        
for row in result:
    print(*row)