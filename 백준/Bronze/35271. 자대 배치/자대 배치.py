import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))

result = [-1]*n
for i in range(n):
    X = list(map(int, input().split())) 
    
    for x in X:
        if A[x] > 0:
            A[x] -= 1
            result[i] = x
            break
        
print(*result)
    